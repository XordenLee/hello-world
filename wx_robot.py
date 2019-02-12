#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Author : XordenLee
# @Time   : 2019/2/1 18:51


import itchat
import requests
import sys

default_api_key = 'bb495c529b0e4efebd5d2632ecac5fb8'

def send(user_id, input_text, api_key=None):
    if not api_key:
        api_key = default_api_key
    msg = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": input_text
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                }
            }
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": user_id
        }
    }

    return requests.post('http://openapi.tuling123.com/openapi/api/v2',json=msg).json()


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg.FromUserName[-9:], msg.text)
    req = send(msg.FromUserName[1: 32], msg.text)
    a = req.get('results')
    b = a[0]['values']['text']
    print(msg.get('ToUserName')[-9:],b)
    return b

itchat.auto_login(hotReload=True)
itchat.run()
