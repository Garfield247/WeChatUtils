# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "b0ebd47415f44860978f1f3d15aa8f97"
    api_key2 = "3610915f73584a239537a81ed887fdce"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "【T】" + result["text"]

bot = Bot(console_qr=True, cache_path=True)

@bot.register()
def forward_message(msg):
    return auto_reply(msg.text)

embed()
