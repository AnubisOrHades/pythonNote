import re
import json
import requests
from lxml import etree


def get_url(start_url):
    ze = r'<a( target="_blank")? href="(.*?html)">((联盟委托|关卡|联盟)\w+-\d+)</a>'
    links = {}
    html = requests.get(start_url)
    html.encoding = "gb2312"
    if html.status_code == 200:
        url_list = re.compile(ze).findall(html.text)
        for url in url_list:
            if "盟" in url[2][-4:] or "卡" in url[2][-4:] or "托" in url[2][-4:]:
                links["盟" + url[2][-3:]] = url[1]
                # print(url[2][-3:],":",url[1])
            else:
                # print(url[2][-4:],":",url[1])
                links["盟" + url[2][-4:]] = url[1]
    return links


def get_content(url):
    result = []
    html = requests.get(url)
    html.encoding = "gb2312"
    html = etree.HTML(html.text)
    lis = html.xpath('//font/p/text()')
    for c in lis[3:]:
        # title = c.xpath("./div/p//a/b/text()")[0]
        c = str(c)
        # if "：" in c:
        #     if len(c.split("："))>2:
        #         print(c)
        #         print(c.split("："))
        #     c = c.split("：")[1:]
        #     c="".join(c)
        clothes_list = []
        for clothes in c.split(">"):
            clothes = re.sub('\(.*?\)$', "", clothes)
            clothes_list.append(clothes)

        result.append(clothes_list)
    return result


def run():
    start_url = "http://news.4399.com/gonglue/qjnn/dapeishi/m/575911.html"
    dapei = {}
    links = get_url(start_url)
    for k, v in links.items():
        # print(k, ":", v)
        dapei[k] = get_content(v)

    with open("dapei.json", "w+", encoding='utf-8')as f:
        # print(str(dapei))
        f.write(str(dapei))


if __name__ == '__main__':
    start_url = "http://news.4399.com/gonglue/qjnn/dapeishi/m/575911.html"

    # print(get_url(start_url))
    # get_content("http://news.4399.com/qjnn/dapeishi/m/803881.html")
    run()
