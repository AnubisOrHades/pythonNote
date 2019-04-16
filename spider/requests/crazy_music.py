import requests
from fake_useragent import UserAgent


class Music:
    host = "http://music.ifkdy.com/"
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "39",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "UM_distinctid=169e72a4d7d48-0b215cb425d991-6313363-144000-169e72a4d7e7e5; CNZZDATA1261550119=1707531591-1554358633-%7C1555377416; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1554361503,1555380217; Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1555381511",
        "Host": "music.ifkdy.com",
        "Origin": "http",
        "Referer": "http",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
    }
    h = {
        "Accept-Encoding": "identity;q=1, *;q=0",
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    }

    def __init__(self, kw, t, path=None):
        if path is None:
            path = r"D:\Anubis\Music"
        self.keyWord = kw
        self.station = t
        self.path = path

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

    def request_data(self, data=None):
        if data is None:
            data = self.form_data()
        data = requests.post(self.host, headers=self.agent(), data=data).json()
        return data

    def down_load(self, page=1):
        data = self.form_data()
        data["page"] = page
        data = self.request_data(data)["data"]
        for music in data:
            self.h["Referer"] = music["url"]
            music_content = requests.get(music["url"], headers=self.h).content
            with open("%s\%s.mp3" % (self.path, music["title"]), "wb")as f:
                f.write(music_content)

            print(music["title"], "下载完成")

    def down_all(self):
        for p in range(10):
            self.down_load(p)


def headder(h):
    for i in h.split("\n"):
        j = i.split(":")
        print('"{}":"{}",'.format(j[0], j[1]))


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
    dd = Music("麦振鸿", "netease", "D:\Anubis\Music\麦振鸿")
    dd.down_all()
