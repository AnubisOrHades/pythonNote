import sys
import os

import requests
from lxml import etree
from fake_useragent import UserAgent
from you_get import common as you_get  # 导入you-get库


def get_bili_link(link):
    """
    获取真实链接
    :param link: 链接
    :return:
    """
    try:
        headers = {
            'User-Agent': UserAgent().chrome
        }
        response = requests.get(link, headers=headers)
        document = etree.HTML(response.text)
        url = document.xpath('//meta[@itemprop="url"]/@content')[0]
        print(url)
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return url
        pass
    finally:
        pass


def down_load(local_path, url, name=None):
    """
    使用you_get下载视频到本地
    :param local_path: 保存地址
    :param name:文件名
    :param url: 视频连接
    :return:
    """
    try:
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        print("开始".center(120, "="))
        sys.argv = ['you-get', '-o', local_path, "-O", name, url]  # sys传递参数执行下载，就像在命令行一样
        you_get.main()
        print("下载完成".center(120, "="))
    except Exception as e:
        print(e, "\n", url)
        return 0
    else:
        return 1


def down_b_video(path=None, url=None, start=1, end=9):
    """
    下载B站视频
    :param path: 本地保存地址
    :param url: 下载链接
    :param start: 开始位置
    :param end: 结束位置
    :return:
    """
    task_lis = ["{}{}".format(url[:-1], i) for i in range(start, end)]
    print(task_lis)
    for task in task_lis:
        try:
            down_load(path, task)
        except Exception as e:
            print("Error:{}".format(e))
    # 删除xml文件
    for root, dirs, files in os.walk(path):
        if root == path and dirs.__len__() == 0:
            for f in files:
                if f.split(".")[-1] == "xml":
                    print(f)
                    os.remove(r"{}\{}".format(path, f))


def run(local_path, url):
    t = type(url)
    if t is list:
        for u in url:
            try:
                down_load(local_path, u)
            except Exception as e:
                print("Error:{}\nErrorUrl:{}".format(e, u))
    elif t is str:
        try:
            down_load(local_path, url)
        except Exception as e:
            print("Error:{}\nErrorUrl:{}".format(e, url))
    else:
        print("url参数错误！！！")


if __name__ == '__main__':
    down_load_path = "F:\\Video\\Web前端1000集全套视频带项目"
    down_url = "https://www.bilibili.com/video/av625463848/?p=8"
    # run(path, urlList)
    down_load("D:\\", "https://www.bilibili.com/video/av969676820/")
    # down_b_video(path, url, start=1, end=107)
