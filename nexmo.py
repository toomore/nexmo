# -*- coding: utf-8 -*-
import requests
import setting

text = u'這是一封測試簡訊 This a test SMS.'
endpoint = 'https://rest.nexmo.com/sms/json'

data = {
    'api_key': setting.api_key,
    'api_secret': setting.api_secret,
    'from': setting.msg_from,
    'to': setting.msg_to,
    'type': 'unicode',
    'text': text*2 + str(len(text*2)),
}

r = requests.post(endpoint, data=data)
print r.text
