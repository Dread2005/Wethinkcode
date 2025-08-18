import sys

import requests

api_key = '9aca7c7f5725a2856bdba10d4f8beaa662a5556ec59289c3e857968771bc709c'
req = 'https://rest.coincap.io/v3/assets?apiKey=9aca7c7f5725a2856bdba10d4f8beaa662a5556ec59289c3e857968771bc709c'

def val_func():
    try:
        value = float(input('Enter number here:'))
        #print(value)
        if type(value) ==  float:
            return value
        else:
            raise ValueError
    except ValueError:
        print('Not A Float')
        return val_func()

val = val_func()
try:
    parameters = {
        'id': 'bitcoin',
        'symbol': 'BTC',
        'currencySymbol': 'B',
        'name':'Bitcoin'
    }
    bit_json = requests.get(req, parameters).json()

    for n in bit_json['data']:
        if n['id'] == 'bitcoin':
            #print(n)
            val_ = float(n['priceUsd']) * val
            print(f'${val_:,.4f}')
except requests.RequestException:
    sys.exit('Request Failed!!!')