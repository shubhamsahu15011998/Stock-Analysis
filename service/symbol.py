import pandas as pd

from DB.utility import DBUtils
from models.symbol import Symbol as SymbolModel


class Symbol:

    @classmethod
    def insert(cls, df: pd.DataFrame) -> bool:
        symbols = [
            SymbolModel(scrip_code=str(obj.get("scrip_code", "")), trading_symbol=str(obj.get("trading_symbol", "")),
                        description=str(obj.get("description", "")), instrument_type=int(obj.get("instrument_type", 0)))
            for obj in df.to_dict(orient='records')]
        DBUtils.bulk_upsert(symbols)
        return True

