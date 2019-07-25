import time, random

import requests
from lxml import etree

host = "https://www.781ii.com"


def down_mp3(url, path):
    html = requests.get(url)
    name = path + "\\" + url.split("/")[-1]
    with open(name, "wb")as f:
        f.write(html.content)
    print(url)


def mp3_link(url):
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = "utf-8"
        html = etree.HTML(html.text)
        lis = html.xpath('//video/source/@src')[0]
        return lis
    else:
        return html.status_code


def link(url):
    try:
        html = requests.get(url)
        if html.status_code == 200:
            html.encoding = "utf-8"
            html = etree.HTML(html.text)
            lis = html.xpath('//div[@class="box list channel list-text-my"]/ul/li')
            for i in lis:
                h = i.xpath("./a/@href")[0]
                with open("maomi_voice.txt", "a")as f:
                    f.write(host + h + "\n")
        else:
            print("Error url:" + url)
    except Exception as e:
        print(e)
        print("Error url:" + url)


def run(path):
    # urls = ["https://www.781ii.com/yousheng/list-诱惑短篇小说-%d.html" % i for
    #         i in range(1, 90)]
    # # voice_urls = []
    # for i in urls:
    #     link(i)
    #     print(i)
    with open("maomi_voice.txt", "r")as f:
        for i in range(1774):
            u = f.readline()[:-1]
            # print(u, "\n", "https://www.781ii.com/yousheng/40481.html")
            # print(u == "https://www.781ii.com/yousheng/40481.html")
            # print(mp3_link(u))
            try:
                down_mp3(mp3_link(u), path)
            except:
                print(i)
    # for voice_url in voice_urls:
    #     down_mp3(mp3_link(voice_url), path)


if __name__ == '__main__':
    run(r"D:\Anubis\Music\cat\短篇小说")
    # print(mp3_link("https://www.781ii.com/yousheng/40481.html"))
    """82-----87   123"""
    pass
