from io import BytesIO, StringIO
import logging
from typing import Any, Dict, Optional

import pandas as pd
from tgedr.nihao.s3.s3_connector import S3Connector
from tgedr.nihao.sink.sink import Sink, SinkException

logger = logging.getLogger(__name__)


class PdDataFrameS3Sink(S3Connector, Sink):
    __DEFAULT_FORMAT: str = "parquet"
    __CSV_HEADER: bool = True

    def __init__(self, config: Optional[Dict[str, Any]] = None):
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
                logger.info(f"[put] file {file_name} exists, going to delete")
                self._resource.Object(bucket_name, file.key).delete()

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
