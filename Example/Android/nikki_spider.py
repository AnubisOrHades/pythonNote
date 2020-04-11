import requests
from lxml import etree
from db.MongoDB.pm import MongodbClient

db = MongodbClient(db="SpiderData", table="nikki_guide")

key_word = ["属性", "技能推荐", "TAG", "要求属性", "对方技能", "注", "下一关", "NPC技能", "背景", "tag", "推荐技能", "tag：海军风"]


def barrier(url=None):
    result = []
    try:
        if not url:
            url = "http://news.4399.com/gonglue/qjnn/dapeishi/m/575911.html"
        html = requests.get(url)
        html.encoding = "gb2312"
        html = etree.HTML(html.text)
        lis = html.xpath('//font/a')
        for l in lis:
            if l.xpath("./text()").__len__() <= 0:
                continue
            title = l.xpath("./text()")[0]
            if "联盟" in title or "关卡" in title:
                barrier_url = l.xpath("./@href")[0]
                result.append({"barrier_txt": title, "barrier_url": barrier_url})
            else:
                continue

    except Exception as e:
        print("Error:{}".format(e))
        return []
    else:
        return result
        pass
    finally:
        pass


def guide_text(task):
    try:
        result = []
        html = requests.get(task["barrier_url"])
        html.encoding = "gb2312"
        html = etree.HTML(html.text)
        lis = html.xpath('//font/p')
        if lis.__len__() < 8:
            lis = html.xpath('//div[@class="content"]/p')
        for l in lis:
            strong = l.xpath('./strong/text()')
            txt = []
            title = None
            if strong.__len__() <= 0:
                text = l.xpath('./text()')
                if text:
                    if ":" in text[0]:
                        text = text[0].split(":")
                    elif "：" in text[0]:
                        text = text[0].split("：")
                    else:
                        continue
                if text.__len__() > 0:
                    title = text[0]
                    if text.__len__() > 1:
                        for t in text[1].split(">"):
                            if "(" in t:
                                t = t.split("(")[0]
                            txt.append(t)
            else:
                title = strong[0]
                txts = l.xpath('./text()')
                if txts.__len__() > 0:
                    for t in txts[0].split(">"):
                        if "(" in t:
                            t = t.split("(")[0]
                        txt.append(t)
            if title is None or txt.__len__() == 0:
                continue
            result.append({"title": title, "txt": txt})

    except Exception as e:
        print("Error:{}".format(e))
    else:
        guide = {"_id": task["barrier_txt"]}

        for i in result:
            i["title"] = i["title"].strip()
            i["title"] = i["title"].strip(":")
            i["title"] = i["title"].strip("：")
            i["title"] = i["title"].replace("*", "·")
            if i["title"] in key_word:
                continue
            guide[i["title"]] = i["txt"]
        db.save(guide)
        return guide
    finally:
        pass


def run():
    try:
        for i in barrier():
            print(i)
            guide_text(i)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    """"""

    url="https://shouyou.3dmgame.com/zt/389_gl_gkgl_1043_1/"
    xpath='//div[@class="info"]/ul/li/a'
    # run()
    # guide_text({"barrier_txt": 12, "barrier_url": "http://news.4399.com/gonglue/qjnn/dapeishi/m/599194.html"})
    for i in db.select():
        print(i)
