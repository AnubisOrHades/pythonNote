import requests
from lxml import etree
import tqdm
from photos import get_host
from tqdm import tqdm


# HOST = get_host()
# urls = ["https://{}/shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95-{}.html".format(HOST, i) for i in range(1, 51)]


def search(url, keyword="痴"):
    html = requests.get(url)
    html.encoding = "utf8"
    html = etree.HTML(html.text)
    lis = html.xpath('//ul[@class="img-list-data"]//li/a')
    for a in lis:
        link = a.xpath("./@href")[0]
        title = a.xpath("./@title")[0]
        if keyword in title:
            print("{}:https://{}{}".format(title, HOST, link))


tasks = ["https://s1.maomibf1.com/common/zw/2019_02/17/zw_HJDbpYML_wm/zw_HJDbpYML_wm{}.ts".format(i) for i in
         range(1, 1169)]


def down(i):
    url = "https://maomibf2.com/common/zw/2019_02/17/zw_HJDbpYML_wm/zw_HJDbpYML_wm{}.ts".format(i)
    html = requests.get(url)
    with open("{}\{}.ts".format(PATH, i), "w")as f:
        f.write(str(html.content))


"""
https://www.aly7.com/shipin/play-32351.html?road=2
"""
if __name__ == '__main__':
    PATH = r"D:\FFOutput\女大生痴汉电车"
    # for i in tqdm(range(0,1169)):
    #     # print(i)
    #     # search(i,"女大生")
    #     down(i)
    sss = """
POST http://api.ippzone.com/index/recommend?sign=d66ff7787c416337bdb4b96a858c4eda HTTP/1.1
Request-Type: text/json
ZYP: mid=426409910291
did: ab99b33bda759869
Dev-Type: android
App-Ver: 4.9.4
Content-Type: text/plain; charset=utf-8
Content-Length: 459
Host: api.ippzone.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.12.1

{"ad_wakeup":1,"audio":1,"auto":0,"c_types":[1,2,101,102,103,104,105,20,21,22,23,8],"direction":"down","filter":"all","sdk_ver":{},"tab":"推荐","h_av":"4.9.4","h_pipi":"1.9.4","h_dt":0,"h_os":22,"h_app":"zuiyou_lite","h_model":"vivo X6S A","youth_mode":0,"h_did":"ab99b33bda759869","h_nt":1,"h_m":426409910291,"h_ch":"vivo","h_ts":1569218922798,"token":"T2K9Na-LV8dQQK4Q9blJ_K2NAbV3Slac8p_rbXdYF3yatieT2mrE40NIyQBR3T8Z_HvmU","android_id":"ab99b33bda759869"}
"""
    header = {
        'Request-Type': 'text/json',
        'ZYP': 'mid=426409910291',
        'did': 'ab99b33bda759869',
        'Dev-Type': 'android',
        'App-Ver': '4.9.4',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Length': '457',
        'Host': 'api.ippzone.com',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.1'
    }
    s = {
        "Request-Type": "text/json",
        "ZYP": "mid=426409910291",
        "did": "ab99b33bda759869",
        "Dev-Type": "android",
        "App-Ver": "4.9.4",
        "Content-Type": "text/plain; charset=utf-8",
        "Content-Length": "459",
        "Host": "api.ippzone.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.1",
    }
    p = {
        "ad_wakeup": 1,
        "audio": 1,
        "auto": 0,
        "c_types": [1, 2, 101, 102, 103, 104, 105, 20, 21, 22, 23, 8],
        "direction": "down",
        "filter": "all",
        "sdk_ver": {},
        "tab": "推荐",
        "h_av": "4.9.4",
        "h_pipi": "1.9.4",
        "h_dt": 0,
        "h_os": 22,
        "h_app": "zuiyou_lite",
        "h_model": "vivo X6S A",
        "youth_mode": 0,
        "h_did": "ab99b33bda759869",
        "h_nt": 1,
        "h_m": 426409910291,
        "h_ch": "vivo",
        "h_ts": 1569218922798,
        "token": "T2K9Na-LV8dQQK4Q9blJ_K2NAbV3Slac8p_rbXdYF3yatieT2mrE40NIyQBR3T8Z_HvmU",
        "android_id": "ab99b33bda759869"
    }
    html = requests.post("http://api.ippzone.com/index/recommend?sign=d66ff7787c416337bdb4b96a858c4eda",
                         headers=s,
                         data=p
                         )
    print(html.json())
    """
    POST http://api.ippzone.com/ad/fetch_splash?sign=fb892361b5dc80ef7f23c8ae3115392d HTTP/1.1
Request-Type: text/json
ZYP: mid=426409910291
did: ab99b33bda759869
Dev-Type: android
App-Ver: 4.9.4
Content-Type: text/plain; charset=utf-8
Content-Length: 540
Host: api.ippzone.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.12.1

{"ad_wakeup":0,"adslot":"4000","h_ua":"Mozilla\/5.0 (Linux; Android 5.1.1; vivo X6S A Build\/LMY47V) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/39.0.0.0 Mobile Safari\/537.36","num":1,"resolution":"1080x1920","h_av":"4.9.4","h_pipi":"1.9.4","h_dt":0,"h_os":22,"h_app":"zuiyou_lite","h_model":"vivo X6S A","youth_mode":0,"h_did":"ab99b33bda759869","h_nt":1,"h_m":426409910291,"h_ch":"vivo","h_ts":1569226802778,"token":"T1KeNa-LV8dQQK4Q9blJ_K2NAbWJwWnEQULmhIOvjcl-L4BTXGVKYNmEgs35E6_rKjipd","android_id":"ab99b33bda759869"}
    """

"""
https://browser.vivo.com.cn/client/news/recommend.do?loadTimes=2&tbs=&refreshType=0&topNewsVersion=&screensize=1080*1920&timeInterval=62224&timestamp=1569230712342&adrVerName=5.1.1&appId=142&pixel=480&clientPackage=com.vivo.browser&u=11010030363447333000fe3f69091300&isVFans=false&imei=861467032669318&nt=wifi&clientVersion=16030&udid=861467032669318&sysver=PD1415BA_PD1415BAMA_3.13.1&firstAccessTime=0&freeWiFiRefresh=0&featureUpgradeVersion=1&elapsedtime=309371505&pver=0&av=22&an=5.1.1&openudid=ab99b33bda759869&make=vivo&location=121.438761*31.221765&recommendType=2&ua=Mozilla%2F5.0+%28Linux%3B+Android+5.1.1%3B+vivo+X6S+A+Build%2FLMY47V%3B+wv%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F62.0.3202.84+Mobile+Safari%2F537.36+VivoBrowser%2F6.6.3.0&ip=192.168.1.135&uid=00000000-4c49-2c9e-9ad8-46ee4e911b4a&resolution=1920*1080&netType=wifi&sourceAppend=eyJzY2VuZSI6IjIwMDAiLCJmcm9taWQiOiIwIn0%3D&ver=16030&scene=0&model=vivo+X6S+A&s=2%7C1481138236
https://open.toutiao.com/a6732126933754102276/?utm_campaign=open&utm_medium=webview&utm_source=vivoliulanqi&item_id=6732126933754102276&req_id=2019092317253001000806317216263&dt=vivo+X6S+A&label=funny&gy=f6e525ea5de6dd553aee14e79dab70c87cb051d38c40c50b93566939ad655d9b33f9efd7ae4e579e2892b81643b78cd8ea87b7d55c248ede9e22f6632bbb962a4307838d71593405bc6ac7a89d6e3c84cf8fe29956b0a90d378bcae58aac74b7ab354a9ee492a73bc40531bd3546984f13ab8452ee18789c6008dbe0be9999f4&crypt=8392&isNews=1&showComments=0&showOriginalComments=true
https://open.toutiao.com/comments/v2/?group_id=6732126933754102276&tab_index=0&offset=0&count=12&service_id=
"""
