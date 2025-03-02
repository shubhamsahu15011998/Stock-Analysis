import pandas as pd

from DB.utility import DBUtils
from models.symbol import Symbol as SymbolModel


class Symbol:

    @classmethod
    def insert(cls, df: pd.DataFrame) -> bool:
        data = df.to_dict(orient='records')
        print("Data Length : ", len(data))
        DBUtils.bulk_upsert(SymbolModel, data, ["trading_symbol"])
        return True

    # @classmethod
    # def get_all(cls):
    #     return SymbolModel.objects
