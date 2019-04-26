import time, random

import requests
from lxml import etree
import threadpool

from db.MongoDB.pm import MongodbClient


def threadingpool(fun, lis, n=10):
    """
    线程池
    :param fun: 执行方法
    :param lis: 方法参数列表
    :param n: 线程个数
    :return:
    """
    pool = threadpool.ThreadPool(n)
    threadList = threadpool.makeRequests(fun, lis)
    [pool.putRequest(req) for req in threadList]
    pool.wait()


class IP:
    mongoClient = MongodbClient(db="SpiderData", table="IP")

    def __init__(self, h, p, s, t="http"):
        self.ip = h
        self.port = p
        self.time = s
        self.type = t

    def __str__(self):
        print(self.ip, ":", self.port, "\t", self.time)

    def proxy(self):
        return {self.type: "{}:{}".format(self.ip, self.port)}

    def save(self):
        """
        如果代理ip可用，且响应时间小于等于1秒，则保存进mongoDB数据库
        :return:
        """
        if len(self.time) > 0 and float(self.time) < 2 and self.test_ip(self):
            # if self.test_ip(self):
            self.mongoClient.save(_id="{}:{}".format(self.ip, self.port), ip=self.ip, port=self.port, time=self.time,
                                  type=self.type)
            print("successful!")

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
            print("Error:", e)
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


def get_kuai_ip(url):
    """
    https://www.kuaidaili.com/free/inha/2/
    爬取快代理的免费代理
    :param url: 网页
    :return:
    """
    while 1:
        proxy_ip = random.choice(pool)
        ip = IP(proxy_ip["ip"], proxy_ip["port"], proxy_ip["time"])
        if ip.test_ip(ip):
            html = requests.get(url, proxies=ip.proxy(), timeout=5)
            html = etree.HTML(html.text)
            lis = html.xpath('//*[@id="list"]/table/tbody/tr')
            for l in lis:
                h = l.xpath("./td[1]/text()")[0]
                p = l.xpath("./td[2]/text()")[0]
                s = l.xpath("./td[6]/text()")[0][:-1]
                t = l.xpath("./td[4]/text()")[0]

                ip = IP(h, p, s, t)
                # print(ip)
                ip.save()
            break


def get_qydaili_ip(url):
    """
    "http://www.qydaili.com/free/?action=china&page=1"
    :param url:
    :return:
    """
    n = 0
    while 1:
        # proxy_ip = random.choice(pool)
        # proxy = IP(proxy_ip["ip"], proxy_ip["port"], proxy_ip["time"])
        proxy = IP("35.221.133.32", "3128", 1)
        if proxy.test_ip(proxy):
            # print(proxy.proxy())
            try:
                html = requests.get(url, proxies={"https": "35.221.133.32:3128"}, timeout=5)
                html = etree.HTML(html.text)
                lis = html.xpath('//tbody/tr')
                for l in lis:
                    h = l.xpath("./td[1]/text()")[0]
                    p = l.xpath("./td[2]/text()")[0]
                    s = l.xpath("./td[6]/text()")[0][:-1]
                    t = l.xpath("./td[4]/text()")[0]

                    if float(s) < 2 and t == "HTTPS":
                        ip = IP(h, p, s, t)
                        # print(ip)
                        ip.save()
                    else:
                        continue
            except Exception as e:
                print("Error:", e)
            else:
                break
            finally:
                if n > 10:
                    break
                n += 1


def get_ip_pool():
    urls = ["https://www.kuaidaili.com/free/inha/%d/" % n for n in range(1, 2679)]
    pool = threadpool.ThreadPool(10)
    threadList = threadpool.makeRequests(get_kuai_ip, urls)
    [pool.putRequest(req) for req in threadList]
    pool.wait()


def ip_pool():
    m = MongodbClient(db="SpiderData", table="IP")
    ipList = []
    for ip_port in m.select():
        ip = IP(ip_port["ip"], ip_port["port"], ip_port["time"])

        ipList.append(ip)

    pool = threadpool.ThreadPool(4)
    threadList = threadpool.makeRequests(IP.test_ip, ipList)
    [pool.putRequest(req) for req in threadList]
    pool.wait()


if __name__ == '__main__':
    lis = ["http://www.qydaili.com/free/?action=china&page=%d" % (i + 1) for i in range(10)]
    urls = ["https://www.kuaidaili.com/free/inha/%d/" % n for n in range(1, 2679)]
    # for i in urls:
    #     print(i)
    #     get_kuai_ip(i)
    get_ip_pool()
    pass
