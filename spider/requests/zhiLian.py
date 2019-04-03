import requests
import json
from pymongo import MongoClient
import time

conn = MongoClient("localhost", 27017)
db = conn.SpiderData
zl = db.zhilian


def zhilian(url):
    html = requests.get(url)
    data = html.content
    data = str(data, 'utf-8')
    data = json.loads(data)
    data = data["data"]["results"]
    if len(data) == 0:
        print("空路由：", url)
        return "break"
    for d in data:
        d["_id"] = d["number"]
        zl.save(d)


def start():
    crity = {
        "北京": "530", "上海": "538", "深圳": "765", "石家庄": "565", "哈尔滨": "622",
        "广州": "763", "天津": "531", "成都": "801", "杭州": "653", "武汉": "736",
        "大连": "600", "长春": "613", "南京": "635", "济南": "702", "青岛": "703",
        "苏州": "639", "沈阳": "599", "西安": "854", "郑州": "719", "长沙": "749",
        "重庆": "551", "无锡": "636", "宁波": "654", "福州": "681", "厦门": "682",
        "合肥": "664", "惠州": "773"
    }
    for c in crity.values():
        i = 1
        while 1:
            if i == 1:
                url = "https://fe-api.zhaopin.com/c/i/sou?" \
                      "pageSize=90&" \
                      "cityId=%s&" \
                      "workExperience=-1&" \
                      "education=-1&" \
                      "companyType=-1&" \
                      "employmentType=-1&" \
                      "jobWelfareTag=-1&" \
                      "kw=Python&" \
                      "kt=3&" \
                      "_v=0.74799541&" \
                      "x-zp-page-request-id=d139e6630673447883c07668887982c5-1552701595756-581927" % c
            else:
                url = "https://fe-api.zhaopin.com/c/i/sou?" \
                      "start=%d&" \
                      "pageSize=%d&" \
                      "cityId=%s&" \
                      "workExperience=-1&" \
                      "education=-1&" \
                      "companyType=-1&" \
                      "employmentType=-1&" \
                      "jobWelfareTag=-1&" \
                      "kw=Python&" \
                      "kt=3&" \
                      "_v=0.74799541&" \
                      "x-zp-page-request-id=d139e6630673447883c07668887982c5-1552701595756-581927" % (
                          i * 90 - 90, 90, c)
            print(("%d  %s" % (i, c)).center(90, '='))
            i += 1
            # print(url)

            try:
                b = zhilian(url)
                if b == "break":
                    break
                time.sleep(10)
            except Exception as e:
                print("Error:%s\n" % e, url)
    print("结束".center(100, '$'))


if __name__ == '__main__':
    start()
