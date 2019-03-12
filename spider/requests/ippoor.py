import requests
import time
from lxml import etree
from pymongo import MongoClient

urls = ["https://www.kuaidaili.com/free/inha/%d/" % n for n in range(1620, 2679)]


class IP:
    def __init__(self, h, p, t):
        self.ip = h
        self.port = p
        self.time = t

    def __str__(self):
        print(self.ip, ":", self.port, "\t", self.time)

    def save(self):
        """
        存储代理 MongoDB数据库
        :return:
        """
        conn = MongoClient("localhost", 27017)
        db = conn.IPProxys
        ip = db.IP
        ip.save({
            "ip": self.ip,
            "port": self.port,
            "time": self.time
        })

    def save_txt(self):
        """
        存储代理为TXT文本
        :return:
        """
        with open("ipList.txt", "a")as f:
            f.write('ip: {},\tport: {},\ttime: {}\n'.format(self.ip,self.port,self.time))


def poor(url):
    """
    爬取快代理的免费代理
    :param url: 网页
    :return:
    """
    html = requests.get(url)
    html = etree.HTML(html.text)
    lis = html.xpath('//*[@id="list"]/table/tbody/tr')
    for l in lis:
        h = l.xpath("./td[1]/text()")[0]
        p = l.xpath("./td[2]/text()")[0]
        t = l.xpath("./td[6]/text()")[0][:-1]

        ip = IP(h, p, t)
        ip.save_txt()


if __name__ == '__main__':
    for u in urls:
        print(u)
        poor(u)
        # time.sleep(10)
