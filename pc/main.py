# -*- coding: utf8 -*-

import requests
import random
import json

# 配置信息
phone = ""  # 登录手机号
password = ""  # 登录密码
desc = "我在这里"  # 签到文本
longitude = "116.404267"  # 经度
latitude = "39.910131"  # 纬度
address = "天安门广场"  # 签到地点名
stateType = "START"  # START 上班 END 下班
# 配置信息

loginUrl = "https://api.moguding.net:9000/session/user/v1/login"
saveUrl = "https://api.moguding.net:9000/attendence/clock/v1/save"
planUrl = "https://api.moguding.net:9000/practice/plan/v1/getPlanByStu"

class Login:
    def PostUrl(self,url, headers, data):
        requests.packages.urllib3.disable_warnings()
        resp = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        return resp.json()

    def GetToken(self):
        data = {
            "password": password,
            "loginType": "android",
            "uuid": "",
            "phone": phone
        }
        resp = self.PostUrl(loginUrl, data=data, headers={"Content-Type": "application/json; charset=UTF-8",
                                                     'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36'})
        return resp['data']['token']

    def GetPlanId(self,headers):
        data = {"state": ""}
        resp = self.PostUrl(planUrl, headers, data)
        return resp['data'][0]['planId']



if __name__ == "__main__":
    login = Login()
    def main():
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
            'roleKey': 'student',
            'Authorization': login.GetToken()
        }

        data = {
            'device': 'Android',
            'address': address,
            'description': desc,
            'country': '',
            'province': '',
            'city': '',
            'longitude': longitude,
            'latitude': latitude,
            'planId': login.GetPlanId(headers),
            'type': stateType
        }

        resp = login.PostUrl(saveUrl, headers, data)
        print(resp)
    main()
