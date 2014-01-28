# -*- coding: utf-8 -*-
import requests
import setting


ENDPOINT = 'https://rest.nexmo.com/sms/json'

def nexmoSMS(data):
    '''
    :param dict data: send data
    :rtype: dict
    :returns: {"message-count":"1","messages":[{"to":"886972xxxxxx","message-id":"0500000004E3EC35","status":"0","remaining-balance":"1.67960000","message-price":"0.01100000","network":"46692"}]}
    '''
    return requests.post(ENDPOINT, data=data).json()

if __name__ == '__main__':
    text = u'這是一封測試簡訊 This a test SMS.'
    data = {
        'api_key': setting.api_key,
        'api_secret': setting.api_secret,
        'from': setting.msg_from,
        'to': setting.msg_to,
        'client-ref': setting.client_ref,
        'type': 'unicode',
        'text': text*2 + str(len(text*2)),
    }
    r = nexmoSMS(data)
    print r
    print type(r)
    print r['messages']
