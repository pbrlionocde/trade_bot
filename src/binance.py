from typing import Final

import requests

API_URL: Final = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT'

def get_bnb_price():
    return requests.get(API_URL).json()


print(get_bnb_price())
