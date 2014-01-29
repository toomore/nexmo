# -*- coding: utf-8 -*-
import requests
import setting


class nexmoSMS(object):
    def __init__(self, api_key, api_secret, _from, to, text, _type='unicode',
            status_report_req=0, client_ref=''):
        '''
        :param dict data: send data
        :rtype: dict
        :returns: {"message-count":"1","messages":[{"to":"886972xxxxxx","message-id":"0500000004E3EC35","status":"0","remaining-balance":"1.67960000","message-price":"0.01100000","network":"46692"}]}
        '''
        self.endpoint = 'https://rest.nexmo.com/sms/json'
        self.data = {
            'api_key': api_key,
            'api_secret': api_secret,
            'from': _from,
            'to': to,
            'client-ref': client_ref,
            'type': _type,
            'text': text,
        }
        self.sms = None

    def send(self):
        ''' Do send sms

            :rtype: dict
            :returns: Nexmo response
        '''
        self.sms = requests.post(self.endpoint, data=self.data)
        ##self.sms.raise_for_status()
        ##return self.sms.status_code
        return self.sms.json()

if __name__ == '__main__':
    text = u'這是一封測試簡訊 This a test SMS.'
    data = {
        'api_key': setting.api_key,
        'api_secret': setting.api_secret,
        #'_from': setting.msg_from,
        '_from': setting.msg_to,
        'to': setting.msg_to,
        'text': text*2 + str(len(text*2)),
        'client_ref': setting.client_ref,
    }

    r = nexmoSMS(**data)
    print 'send:', r.send()
    print 'type of sms:', type(r.sms)

    for i in dir(r.sms):
        print i, getattr(r.sms, i)

