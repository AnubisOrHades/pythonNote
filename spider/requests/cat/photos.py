import os
import time
import queue
import json

import tqdm
import threadpool
import requests
from lxml import etree

from db.MongoDB.pm import MongodbClient


def get_host(url="https://www.766uy.com/enter/pc.html"):
    """
    获取猫咪社区主机地址
    :param url:
    :return: 主机地址
    """
    html = requests.get(url)
    host = html.url.split("/")[2]
    print("https://" + host)
    return host


def compilation(host):
    """
    获取套图集合连接，存入MongoDB数据库
    :param host: 主机地址
    :return: 连接字典
    """
    db = MongodbClient(db="cat", table="magazine")
    compilation_dic = {}
    html = requests.get("https://" + host + "/meinv/index.html")
    html.encoding = "utf8"
    html = etree.HTML(html.text)
    lis = html.xpath('//ul[@class="img-list-data"]//a[@target="_blank"]')
    for a in lis:
        link = a.xpath("./@href")[0]
        title = a.xpath("./@title")[0]
        compilation_dic[title] = link
        db.save(_id=link, magazine=title, url=link)

    return compilation_dic


def get_photos(task):
    """
    获取套图连接，存入MongoDB
    :param task: 任务，套图种类信息，从数据库获取
    :return:
    """
    db = MongodbClient(db="cat", table="album")
    if type(task) is dict:
        url_list = ["https://{}-{}.html".format(HOST + task["url"][:-5], index) for index in range(1, 120)]
    else:
        url_list = ["https://{}-{}.html".format(task[:-5], index) for index in range(1, 120)]
    for url in url_list:
        try:
            html = requests.get(url)
            print(url, "\n\t", html.url)
            html.encoding = "utf8"
            html = etree.HTML(html.text)
            lis = html.xpath('//div[@id="tpl-img-content"]//a[@target="_blank"]')
            if len(lis) == 0:
                print("0" * 100)
                break
            for pl in lis:
                link = pl.xpath("./@href")[0]
                title = pl.xpath("./@title")[0]
                db.save(_id=link, magazine=task["magazine"], album=title, url=link, down=False)
        except Exception:
            raise Exception("\033[1;36;40m 错误：{},url:{}".format(task, url))

        time.sleep(1)


def get_album():
    """
    下载所有套图连接
    :return:
    """
    tasks = queue.Queue()
    db = MongodbClient(db="cat", table="magazine")
    date = db.select()
    for d in date:
        tasks.put(d)
    while not tasks.empty():
        task = tasks.get()
        try:
            get_photos(task)
        except Exception as e:
            print(e)
            return e


def get_img(task):
    """
    获取图片连接，并存入MongoDB
    :param task: 套图信息
    :return:
    """
    db = MongodbClient(db="cat", table="imges")
    url = "https://" + HOST + task["url"]
    print(url)
    try:
        html = requests.get(url)
        html.encoding = "utf8"
        html = etree.HTML(html.text)
        lis = html.xpath('//div[@class="content"]/img')
        if len(lis) == 0:
            print("0" * 100)
        for pl in lis:
            link = pl.xpath("./@data-original")[0]
            name = link.split("/")[-1]
            db.save(_id=link, magazine=task["magazine"], album=task["album"], name=name, url=link, down=False)
    except Exception as e:
        print(e, ("\033[40m 错误：{},url:{} \033[0m".format(task, url)))
    else:
        db = MongodbClient(db="cat", table="album")
        db.update(task, {"down": True})


def img_list():
    """
    获取所有图片连接
    :return:
    """
    db = MongodbClient(db="cat", table="album")
    data = db.select(down=False)
    for d in data:
        get_img(d)
        time.sleep(1)


def down_img(task):
    """
    下载图片
    :param task: 图片信息
    :return:
    """
    img_path = r"{}\{}\{}".format(PATH, task["magazine"].strip(), task["album"].strip())
    path = "{}\\{}".format(img_path, task["name"].strip()).strip()
    try:
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        headers = {
            'authority': 'mmtp1.com',
            'method': 'GET',
            # 'path': '/girl/FEILIN/206/35.jpg',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': '__cfduid=dfa4d804c613690656fc71ddb7be2edb71555827117',
            'if-modified-since': 'Tue, 26 Jun 2018 15:59:23 GMT',
            'if-none-match': "5b3262db-3d0c3",
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' \
            }
        data = requests.get(task["url"], headers=headers)
        # print(data.status_code)
        if data.status_code != 200:
            print("Error Url:{}".format(task["url"]))
            return
        print(data.url)
        with open(path, "wb") as f:
            f.write(data.content)
    except Exception as e:
        print("Error Url:{}".format(task["url"]))
        print(e)
    else:
        db = MongodbClient(db="cat", table="imges")
        db.update(task, {"down": True})


def run(n=10, **kwargs):
    """
    多线程下载图片
    :param n: 线程数
    :param kwargs: magazine：杂志名；
    :return:
    """
    print(kwargs)
    db = MongodbClient(db="cat", table="imges")
    tasks = db.select(down=False, magazine=kwargs["magazine"])
    pool = threadpool.ThreadPool(n)
    requests = threadpool.makeRequests(down_img, tasks)
    [pool.putRequest(req) for req in requests]
    pool.wait()


def export():
    """
    导出所有图片信息，json格式
    :return:
    """
    img_dict = {}
    m = MongodbClient(db="cat", table="imges")
    result = m.select()
    for img in result:
        if img["magazine"] in img_dict:
            pass
        else:
            img_dict[img["magazine"]] = {}

        if img["album"] in img_dict[img["magazine"]]:
            pass
        else:
            img_dict[img["magazine"]][img["album"]] = []
        img_path = r"\{}\{}\{}".format(img["magazine"].strip(), img["album"].strip(), img["name"].strip())
        img_dict[img["magazine"]][img["album"]].append(img_path)
        pass
    w = {"name": "nikki",
         "version": "1.0.0",
         "data": img_dict}
    with open("photos.json", "w", encoding='utf8')as f:
        f.write(json.dumps(w, ensure_ascii=False))


if __name__ == '__main__':
    img = {"magazine": "", "album": "", "img": ""}
    PATH = r"D:\Anubis\图片"
    HOST = "https://www.bsu7.com"
    # HOST = get_host()
    # db = MongodbClient(db="cat", table="album")
    # db = MongodbClient(db="cat", table="magazine")
    # db = MongodbClient(db="cat", table="imges")

    run(50,magazine="123")
