# -*- coding: utf-8 -*-
import requests
import setting
from pprint import pprint


def get_price(data):
    endpoint = 'https://rest.nexmo.com/account/get-pricing/outbound'
    return get_json(endpoint, data)

def get_prefix_price(data):
    endpoint = 'https://rest.nexmo.com/account/get-prefix-pricing/outbound'
    return get_json(endpoint, data)

def get_json(endpoint, data):
    return requests.get(endpoint, params=data).json()

if __name__ == '__main__':
    data = {
            'api_key': setting.api_key,
            'api_secret': setting.api_secret,
            'country': 'TW',  #get_price
            'prefix': 886,  #get_prefix_price
           }
    pprint(get_price(data))
    pprint(get_prefix_price(data))
