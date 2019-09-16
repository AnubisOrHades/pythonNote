import requests
from lxml import etree
import tqdm
from photos import get_host
from tqdm import tqdm

HOST = get_host()
urls = ["https://{}/shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95-{}.html".format(HOST, i) for i in range(1, 51)]


def search(url, keyword="痴"):
    html = requests.get(url)
    html.encoding = "utf8"
    html = etree.HTML(html.text)
    lis = html.xpath('//ul[@class="img-list-data"]//li/a')
    for a in lis:
        link = a.xpath("./@href")[0]
        title = a.xpath("./@title")[0]
        if keyword in title:
            print("{}:https://{}{}".format(title, HOST, link))


tasks = ["https://s1.maomibf1.com/common/zw/2019_02/17/zw_HJDbpYML_wm/zw_HJDbpYML_wm{}.ts".format(i) for i in
         range(1, 1169)]


def down(i):
    url="https://maomibf2.com/common/zw/2019_02/17/zw_HJDbpYML_wm/zw_HJDbpYML_wm{}.ts".format(i)
    html = requests.get(url)
    with open("{}\{}.ts".format(PATH,i),"w")as f:
        f.write(str(html.content))

"""
https://www.aly7.com/shipin/play-32351.html?road=2
"""
if __name__ == '__main__':
    PATH = r"D:\FFOutput\女大生痴汉电车"
    for i in tqdm(range(0,1169)):
        # print(i)
        # search(i,"女大生")
        down(i)
