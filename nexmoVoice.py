# -*- coding: utf-8 -*-
import requests
import setting


ENDPOINT = 'https://rest.nexmo.com/tts/json'

def nexmoVoice(data):
    return requests.post(ENDPOINT, data=data).text

if __name__ == '__main__':
    text = u'這是一封測試簡訊 This a test SMS.'
    data = {
        'api_key': setting.api_key,
        'api_secret': setting.api_secret,
        'from': setting.msg_from,
        'to': setting.msg_to,
        'lg': 'zh-cn',
        'text': text*2 + str(len(text*2)),
    }
    print nexmoVoice(data)
