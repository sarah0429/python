# -*- coding: utf-8 -*-
import datetime
import requests
import json

appID = " "  # 微信公众号
appsecret = " "  # 微信公众号


class WeChat():
    def __init__(self, openid, name):
        self.openid = openid
        self.name = name
        self.data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_token(self):
        try:
            payload = {
                'grant_type': 'client_credential',
                'appid': appID,
                'secret': appsecret,
            }
            url = "https://api.weixin.qq.com/cgi-bin/token?"

            try:
                respone = requests.get(url, params=payload, timeout=50)
                access_token = respone.json().get("access_token")
                content = "{'access_token':" + str(access_token) + ",'time':" + str(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "}"

                print("get_token", access_token)
                return access_token
            except Exception as e:
                print(e)
        except Exception as e:
            print("get_token,file", e)

    def post_data(self):
        data = {
            "touser": self.openid,
            "template_id": " ",  # 模板ID
            # "miniprogram":{
            #   "appid":"wx67afc56d7f6cfac0",  #待使用上线小程序appid
            #   "path":"pages/reserve/mgr/mgr"
            # },
            'url': 'http://eswis.gdpu.edu.cn/',  # 跳转打卡链接
            "data": {
                "first": {
                    "value": "您好，puyuma系统现已自动打卡成功！",
                    "color": "#173177"
                },
                "keyword1": {
                    "value": self.name,
                    "color": "#173177"
                },
                "keyword5": {
                    "value": self.data,
                    "color": "#173177"
                },
                "remark": {
                    "value": "点击跳转到打卡系统！",
                    "color": "#173177"
                }
            }
        }
        json_template = json.dumps(data)
        access_token = self.get_token()
        print("access_token--", access_token)
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + access_token
        try:
            respone = requests.post(url, data=json_template, timeout=50)
            # 拿到返回值
            errcode = respone.json().get("errcode")
            print("test--", respone.json())
            if errcode == 0:
                print("模板消息发送成功")
            else:
                print("模板消息发送失败")
        except Exception as e:
            print("test++", e)
