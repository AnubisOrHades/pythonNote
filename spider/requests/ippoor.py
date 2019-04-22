import time, random

import requests
from lxml import etree
import threadpool

from db.MongoDB.pm import MongodbClient


class IP:
    mongoClient = MongodbClient(db="SpiderData", table="IP")

    def __init__(self, h, p, t):
        self.ip = h
        self.port = p
        self.time = t

    def __str__(self):
        print(self.ip, ":", self.port, "\t", self.time)

    def proxy(self):
        return {"http": "{}:{}".format(self.ip, self.port)}

    def save(self):
        """
        如果代理ip可用，且响应时间小于等于1秒，则保存进mongoDB数据库
        :return:
        """
        # if len(self.time) > 0 and float(self.time <= 1) and self.test_ip(self):
        if self.test_ip(self):
            self.mongoClient.save(ip=self.ip, port=self.port, time=self.time)
            print("suseurll!")

    def delete(self):
        """
        删除代理ip
        :return:
        """
        ip_port = self.mongoClient.delete(ip=self.ip)
        print(ip_port)

    @staticmethod
    def test_ip(self):
        """
        测试代理ip是否可用
        :param self: ip对象
        :return: 可用返回True，不可用返回False
        """
        proxy = self.proxy()
        try:
            html = requests.get("https://www.baidu.com/", proxies=proxy)
            if html.status_code != 200:
                self.delete()
                print(proxy, "无效代理，予以删除")
                return False
            else:
                # print(proxy, "有效代理")
                return True
        except Exception as e:
            print(e)
            self.delete()
            print(proxy, "无效代理，予以删除")
            return False

    def save_txt(self):
        """
        存储代理为TXT文本
        :return:
        """
        with open("ipList.txt", "a")as f:
            f.write('ip: {},\tport: {},\ttime: {}\n'.format(self.ip, self.port, self.time))


pool = IP.mongoClient.select()
pool = list(pool)


def get_ip(url):
    """
    爬取快代理的免费代理
    :param url: 网页
    :return:
    """
    while 1:
        proxy_ip = random.choice(pool)
        ip = IP(proxy_ip["ip"], proxy_ip["port"], proxy_ip["time"])
        if ip.test_ip(ip):
            html = requests.get(url, proxies=ip.proxy())
            html = etree.HTML(html.text)
            lis = html.xpath('//*[@id="list"]/table/tbody/tr')
            for l in lis:
                h = l.xpath("./td[1]/text()")[0]
                p = l.xpath("./td[2]/text()")[0]
                t = l.xpath("./td[6]/text()")[0][:-1]

                ip = IP(h, p, t)
                ip.save()
            break


def get_ip_pool():
    urls = ["https://www.kuaidaili.com/free/inha/%d/" % n for n in range(1, 2679)]
    pool = threadpool.ThreadPool(100)
    threadList = threadpool.makeRequests(get_ip, urls)
    [pool.putRequest(req) for req in threadList]
    pool.wait()


def ip_pool():
    m = MongodbClient(db="SpiderData", table="IP")
    ipList = []
    for ip_port in m.select():
        ip = IP(ip_port["ip"], ip_port["port"], ip_port["time"])

        ipList.append(ip)

    pool = threadpool.ThreadPool(100)
    threadList = threadpool.makeRequests(IP.test_ip, ipList)
    [pool.putRequest(req) for req in threadList]
    pool.wait()


if __name__ == '__main__':
    # get_ip_pool()
    get_ip("https://www.kuaidaili.com/free/inha/1/")
    pass
