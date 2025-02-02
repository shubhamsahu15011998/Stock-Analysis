import requests
import time

# for keys in ['s', 't', 'o', 'h', 'l', 'c', 'v']:
# for epoch_time in response.get('t'):
#     utc_dt = datetime.fromtimestamp(epoch_time, UTC).replace(tzinfo=pytz.utc)
#     ist_dt = utc_dt.astimezone(pytz.timezone("Asia/Kolkata"))
#     formatted_time = ist_dt.strftime('%Y-%m-%d %H:%M:%S %Z')
#     print(formatted_time)

current_epoch_time = int(time.time())
# print("Current Epoch Time : ", current_epoch_time)


class StockPrice:

    def __init__(self):
        pass

    @staticmethod
    def fetch_stock_data(symbol='COCHINSHIP-EQ', from_date=1577836800, to_date=current_epoch_time):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'origin': 'https://charting.nseindia.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'exch': 'N',
            'tradingSymbol': symbol,
            'fromDate': from_date,
            'toDate': to_date,
            'timeInterval': 1,
            'chartPeriod': 'D',
            'chartStart': 0,
        }
        response = requests.post('https://charting.nseindia.com//Charts/ChartData/', headers=headers, json=json_data)
        return response.json()
