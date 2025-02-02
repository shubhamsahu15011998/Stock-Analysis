from io import StringIO
import pandas as pd
import os
import requests


class Symbols:

    def __init__(self):
        pass

    @staticmethod
    def fetch_symbols():
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        response = requests.get('https://charting.nseindia.com//Charts/GetEQMasters', headers=headers)
        return response.text

    @staticmethod
    def write_symbols(txt_symbols):
        output_file_name = os.environ.get("SYMBOL_FILE_NAME")
        df = pd.read_csv(StringIO(txt_symbols), sep="|")
        df.to_csv(output_file_name)
        print(df.shape)

    @staticmethod
    def refresh_symbols():
        Symbols.write_symbols(Symbols.fetch_symbols())
