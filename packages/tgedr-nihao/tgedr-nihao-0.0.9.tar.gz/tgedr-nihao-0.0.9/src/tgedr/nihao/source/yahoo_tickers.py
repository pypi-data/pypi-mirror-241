import logging
from typing import Any, Dict, List, Optional
import pandas as pd
import logging
import yfinance as yf
from tgedr.nihao.source.source import Source

logger = logging.getLogger(__name__)


class YahooTickersSource(Source):
    __DEFAULT_INTERVAL: str = "1d"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)

    def get(self, key: str, **kwargs) -> pd.DataFrame:
        logger.info(f"[get|in] ({key}, {kwargs})")

        symbols_as_str = key
        symbols: List[str] = [k.strip() for k in symbols_as_str.split(",")]

        interval = self.__DEFAULT_INTERVAL
        if "interval" in kwargs:
            interval = kwargs["interval"]

        start = None
        if "start" in kwargs:
            start = kwargs["start"]

        end = None
        if "end" in kwargs:
            end = kwargs["end"]

        result = pd.DataFrame(columns=["symbol", "variable", "value", "actual_time"])

        market_data = yf.download(symbols_as_str, start=start, end=end, interval=interval)
        if not market_data.empty:
            multiple_symbols: bool = 1 < len(symbols)
            for key, val in market_data.to_dict().items():
                if multiple_symbols:
                    variable, symbol = key
                else:
                    variable = key
                    symbol = symbols[0]

                for ts, num in val.items():
                    if not pd.isnull(num):
                        entry = pd.DataFrame(
                            {"symbol": symbol, "variable": [variable], "value": [num], "actual_time": [ts.timestamp()]}
                        )
                        result = pd.concat([result, entry])

            result.reset_index(drop=True, inplace=True)
            result = result.sort_values(by=["actual_time", "symbol"])

        logger.info(f"[get|out] => {result}")
        return result
