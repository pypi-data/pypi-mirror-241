from abc import ABC, abstractmethod
from io import BytesIO, StringIO
import io
import logging
import os
from typing import Any, Dict, Optional
import pandas as pd
import boto3

logger = logging.getLogger(__name__)


class SinkException(Exception):
    pass


class Sink(ABC):
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._config = config

    @abstractmethod
    def put(self, obj: Any, key: str) -> None:
        raise NotImplementedError()


class Source(ABC):
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._config = config

    @abstractmethod
    def get(self, key: str) -> Any:
        raise NotImplementedError()


class S3Connector:
    def __init__(self):
        self.__resource = None
        self.__session = None
        self.__client = None

    @property
    def _session(self):
        if self.__session is None:
            self.__session = boto3.Session(
                aws_access_key_id=os.environ["AWS_KEY_ID"],
                aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
                region_name=os.environ["AWS_REGION"],
            )
        return self.__session

    @property
    def _resource(self):
        if self.__resource is None:
            self.__resource = self._session.resource("s3")
        return self.__resource

    @property
    def _client(self):
        if self.__client is None:
            self.__client = self._session.client("s3")
        return self.__client


class Parquet2PdDataFrameS3Source(S3Connector, Source):
    def __init__(self, config: Dict[str, Any]):
        S3Connector.__init__(self)
        Source.__init__(self, config)

    def __read_parquet(self, key: str, bucket: str):
        obj = self._client.get_object(Bucket=bucket, Key=key)
        return pd.read_parquet(io.BytesIO(obj["Body"].read()))

    def get(self, key: str) -> pd.DataFrame:
        result: pd.DataFrame = None
        bucket_name = key.split("://")[1].split("/")[0]
        file_path = key.replace("s3://" + bucket_name + "/", "")
        bucket = self._resource.Bucket(bucket_name)

        bucket_paths = [item.key for item in bucket.objects.filter(Prefix=file_path) if item.key.endswith(".parquet")]

        dfs = [self.__read_parquet(path, bucket=bucket_name) for path in bucket_paths]
        result = pd.concat(dfs, ignore_index=True)
        return result


class PdDataFrameS3Sink(S3Connector, Sink):
    __DEFAULT_FORMAT: str = "parquet"
    __CSV_HEADER: bool = True

    def __init__(self, config: Dict[str, Any]):
        S3Connector.__init__(self)
        Sink.__init__(self, config)
        if "format" in config:
            self.__format = config["format"]
        else:
            self.__format = self.__DEFAULT_FORMAT
        if "csv_header" in config:
            self.__csv_header = True if (1 == config["csv_header"]) else False
        else:
            self.__csv_header = self.__CSV_HEADER

    def put(self, obj: pd.DataFrame, key: str):
        """
        puts dataframe directly on S3 as parquet before checking duplicates,
        if file exists already throws SinkException
        Input
            obj: pandas dataframe
            key: S3 file path (s3://<bucket-name>/<file-name>)
        throws:
            SinkException, if file exists already
        """
        logger.info(f"[put|in] ({obj}, {key})")
        bucket_name = key.split("://")[1].split("/")[0]
        file_name = key.replace("s3://" + bucket_name + "/", "")
        bucket = self._resource.Bucket(bucket_name)

        for file in bucket.objects.all():
            if file_name in file.key:
                raise SinkException(f"file {file_name} exists")

        if self.__format == "parquet":
            out_buffer = BytesIO()
            obj.to_parquet(out_buffer, index=False)
        elif self.__format == "csv":
            out_buffer = StringIO()
            obj.to_csv(out_buffer, header=self.__csv_header, index=False)
        else:
            raise SinkException(f"unsupported format: {self.__format}")

        self._client.put_object(Bucket=bucket_name, Key=file_name, Body=out_buffer.getvalue())
        logger.info("[put|out]")
