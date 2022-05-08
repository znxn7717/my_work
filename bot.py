import json
import requests

base_url = 'https://api.kucoin.com'
def cprice(sym, tf):
    url = f'{base_url}/api/v1/market/candles?type={tf}&symbol={sym}'
    res = requests.get(url).text
    kline_data0 = json.loads(res)
    kline_data1 = kline_data0['data']
    closing_price = []
    for i in kline_data1:
        closing_price.append(i[2])
    print(closing_price)


b = input('symbol = ')
blen = len(b)
b2 = b[-4:]
b1 = b[:blen-4]
cprice(f'{b1}-{b2}', input('timeframe = '))