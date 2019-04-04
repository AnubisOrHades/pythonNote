import requests


class Music:
    url = "http://music.ifkdy.com/"
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

    def __init__(self, kw, t):
        self.keyWord = kw
        self.station = t

    def form_data(self):
        data = {"input": self.keyWord,
                "filter": "name",
                "type": self.station,
                "page": 1}
        return data

    def request_data(self):
        data = requests.post(self.url, headers=self.header, data=self.form_data()).json()
        return data

    def down_load(self):
        data = self.request_data()["data"]
        for misic in data:
            music_content = requests.get(misic["url"]).content
            with open("D:\Anubis\Music\多情剑客无情剑\%s.mp3" % misic["title"], "wb")as f:
                f.write(music_content)


dd = Music("多情剑客无情剑", "kuwo")
d = dd.down_load()
