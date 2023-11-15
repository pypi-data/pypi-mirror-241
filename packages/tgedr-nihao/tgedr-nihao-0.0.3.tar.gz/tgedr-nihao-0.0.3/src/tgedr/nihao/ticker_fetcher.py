from abc import ABC, abstractmethod
from datetime import datetime
import logging
from typing import List
from pandas import DataFrame, isnull, concat
import yfinance as yf

logger = logging.getLogger(__name__)


class Fetcher(ABC):
    @abstractmethod
    def fetch(
        self, symbols: List[str], start: datetime = None, end: datetime = None, interval: str = "1d"
    ) -> DataFrame:
        pass


class YahooFetcher(Fetcher):
    def fetch(
        self, symbols: List[str], start: datetime = None, end: datetime = None, interval: str = "1d"
    ) -> DataFrame:
        logger.info(f"[fetch|in] ({symbols}, {start}, {end}, {interval})")

        result = DataFrame(columns=["symbol", "variable", "value", "actual_time"])
        max_actual_time: datetime = None

        market_data = yf.download(",".join(symbols), start=start, end=end, interval=interval)
        if not market_data.empty:
            multiple_symbols: bool = 1 < len(symbols)
            for key, val in market_data.to_dict().items():
                if multiple_symbols:
                    variable, symbol = key
                else:
                    variable = key
                    symbol = symbols[0]

                for ts, num in val.items():
                    if not isnull(num):
                        entry = DataFrame(
                            {"symbol": symbol, "variable": [variable], "value": [num], "actual_time": [ts.timestamp()]}
                        )
                        result = concat([result, entry])

            result.reset_index(drop=True, inplace=True)
            result = result.sort_values(by=["actual_time", "symbol"])

        logger.info(f"[fetch|out] => {result}")
        return result
