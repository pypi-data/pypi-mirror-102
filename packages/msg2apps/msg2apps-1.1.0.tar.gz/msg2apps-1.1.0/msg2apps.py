import requests
import json
import os


def Wechat(msg, corpid, secret, agentid):
    
    data = json.dumps({
            "touser" : "admin",
            "msgtype" : "text",
            "agentid" : agentid,
            "text" : {
                "content" : msg
            },
            "safe":0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        })  
    url_get_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(corpid, secret)
    try:
        token = requests.get(url_get_token, timeout=5).json()["access_token"]
    except Exception as e:
        print(e)
        return
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(token)
    
    try:
        r = requests.post(url, data=data, timeout=5)
        print(r.json()['errmsg'])
        return
    except Exception as e:
        print(e)
        return


def Telegram(msg, token, chat_id):
    
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}>".format(token, chat_id, msg)
    try:
        r = requests.post(url, timeout=5)
        # TUDO
        # print(r.json()['ok'])
        return
    except Exception as e:
        print(e)
        return