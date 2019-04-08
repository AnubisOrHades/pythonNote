import requests
from fake_useragent import UserAgent


class Music:
    host = "http://music.ifkdy.com/"
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "71",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "UM_distinctid=169e72a4d7d48-0b215cb425d991-6313363-144000-169e72a4d7e7e5; CNZZDATA1261550119=1707531591-1554358633-%7C1554358633; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1554361503; Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1554361503",
        "Host": "music.ifkdy.com",
        "Origin": "http://music.ifkdy.com",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://music.ifkdy.com/?name=%E6%B0%B4%E6%9C%88%E6%B4%9E%E5%A4%A9&type=kuwo",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    proxy = {
        'HTTPS': '111.177.176.106:9999'
    }

    def __init__(self, kw, t):
        self.keyWord = kw
        self.station = t

    def agent(self):
        """
        随机agent
        :return:
        """
        ua = UserAgent()
        user_agent = ua.random
        self.header["User-Agent"] = user_agent
        return self.header

    def form_data(self):
        data = {
            "input": self.keyWord,
            "filter": "name",
            "type": self.station,
            "page": 1
        }
        return data

    def request_data(self):
        data = requests.post(self.host, proxies=self.proxy, headers=self.agent(), data=self.form_data()).json()
        return data

    def down_load(self):
        data = self.request_data()["data"]
        for music in data:
            music_content = requests.get(music["url"]).content
            with open("D:\Anubis\Music\多情剑客无情剑\%s.mp3" % music["title"], "wb")as f:
                f.write(music_content)


if __name__ == '__main__':
    music_type = {
        "网易": "netease",
        "qq音乐": "qq",
        "酷我": "kuwo",
        "酷狗": "kugou",
        "虾米": "xiami",
        "百度": "baidu",
        "咪咕": "migu",
        "蜻蜓": "qingting",
        "一听": "1ting",
        "荔枝": "lizhi",
        "喜马拉雅": "ximalaya"
    }
    dd = Music("美人吟", "netease")
    d = dd.request_data()
    print(d)
