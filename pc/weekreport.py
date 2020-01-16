from pc.main import Login
import requests
import json

if __name__ == '__main__':
    login = Login()
    Fjson = open("./weeks.json", encoding='utf-8')
    fjson = json.load(Fjson)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'roleKey': 'student',
        'Authorization': login.GetToken()
    }
    PostGetWeeksJson = {
        "planId": login.GetPlanId(headers)
    }
    re = requests.post(url="https://api.moguding.net:9000/practice/paper/v1/getWeeks1",
                       data=json.dumps(PostGetWeeksJson), headers=headers,verify=False)
    val = json.loads(re.content.decode())
    for key in range(len(val["data"])):
        PostWeekJson = {
            "yearmonth": "",
            "address": "",
            "title": "第" + val["data"][key]["weeks"] + "的周报",
            "longitude": "0.0",
            "latitude": "0.0",
            "weeks": val["data"][key]["weeks"],
            "endTime": val["data"][key]["endTime"],
            "startTime": val["data"][key]["startTime"],
            "planId": login.GetPlanId(headers),
            "reportType": "week",
            "content": fjson[key]["content"]
        }
        result = requests.post(url="https://api.moguding.net:9000/practice/paper/v1/save", data=json.dumps(PostWeekJson),
                               headers=headers,verify=False)
        print(result.text)

    Fjson.close()
