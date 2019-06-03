import requests, time
from lxml import etree


def down_story(url, name, rule, encoding="utf-8"):
    html = requests.get(url)
    html.encoding = encoding
    html = etree.HTML(html.text)
    lis = html.xpath(rule)
    for c in lis:
        print(c)
        with open(name, "a", encoding=encoding)as f:
            f.write(c)


def run():
    url_list = ["http://www.liudatxt.com/so/3874/%d.html" % (1033625 + i) for i in range(365)]

    for u in url_list:
        down_story(u, "修真老师在校园.txt", '//div[@id="content"]/text()')
        time.sleep(10)
