from time import sleep
import os
import shutil
import json

import requests
import jsonpath

from db.MongoDB.pm import *
from tools.down_load.my_get import down_load
from tools.video import preview, de_watermark
from tools.image import get_txt_img, img_shape
from tools.file import File
from tools.down_load import ordinary_down_load

"""
MongoDB state:
    1:已下载；2：已生成预览图（第一帧）；3已清除水印；
"""


class UpVideo(object):
    def __init__(self, mongodb_obj=None, link=None, up=None, aid=None, title=None, length=None, pic=None, state=None):
        """
        UpVideo 初始化
        :param mongodb_obj: MongoDB数据对象
        :param link: 视频连接
        :param up: 视频作者
        :param aid: 视频id
        :param title: 视频标题
        :param length: 视频长度
        :param pic: 视频封面
        :param state: 状态{0：只获取了数据，1：已下载，2：已有封面，3：已去水印}
        """
        if mongodb_obj is None:
            self.link = link
            self.up = up
            self.aid = aid
            self.title = title
            self.length = length
            self.pic = pic
            self.state = state
        else:
            self.link = mongodb_obj.get("link")
            self.up = mongodb_obj.get("up")
            self.aid = mongodb_obj.get("aid")
            self.title = mongodb_obj.get("title")
            self.length = mongodb_obj.get("length")
            self.pic = mongodb_obj.get("pic")
            self.state = mongodb_obj.get("state")
        pass

    def save_to_mongodb(self, mdb):
        """
        存储数据到MongoDB
        :param mdb: MongoDB连接对象
        :return: 存储结果{0：失败，1：成功，9：数据已存在}
        """
        try:
            if mdb.select(aid=self.aid).count() == 0:
                mdb.save({
                    "link": "https://www.bilibili.com/video/av{}/".format(self.aid),
                    "up": self.up,
                    "aid": self.aid,
                    "title": self.title,
                    "length": self.length,
                    "pic": self.pic,
                    "state": 0
                })

            else:
                print(self.aid, "视频已存在")
                return 9
            pass
        except Exception as e:
            print("Error:{}".format(e))
            return 0

        else:
            return 1
            pass
        finally:
            pass

    def __str__(self):
        return "link:{}\nup:{}\naid:{}\ntitle:{}\nlength:{}\npic:{}\nstate:{}".format(self.link, self.up,
                                                                                      self.aid, self.title,
                                                                                      self.length, self.pic,
                                                                                      self.state)


class BilibiliUp(object):
    def __init__(self, name, link, mdb, file_path, preview_path, clean_path):
        self.name = name
        self.link = link
        self.mdb = mdb
        self.file_path = file_path
        self.preview_path = preview_path
        self.clean_path = clean_path

    def get_data(self):
        pn = 1
        while 1:
            try:
                link = self.link.replace("pn=1", "pn={}".format(pn))
                response = requests.get(link)
                result = response.json()["data"]["list"]["vlist"]
                if len(result) == 0:
                    break
                for l in result:
                    UpVideo(
                        link="https://www.bilibili.com/video/av{}/".format(l.get("aid")),
                        up=self.name,
                        aid=l.get("aid"),
                        title=l.get("title"),
                        length=l.get("length"),
                        pic=l.get("pic"),
                        state=0
                    ).save_to_mongodb(self.mdb)
                    # aid = l.get("aid")
                    # if self.mdb.select(aid=aid).count() == 0:
                    #     self.mdb.save({
                    #         "link": "https://www.bilibili.com/video/av{}/".format(l.get("aid")),
                    #         "up": self.name,
                    #         "aid": aid,
                    #         "title": l.get("title"),
                    #         "length": l.get("length"),
                    #         "pic": l.get("pic"),
                    #         "state": 0
                    #     })
                    # else:
                    #     print("视频已存在")
                pass
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pn += 1
                pass
            finally:
                sleep(5)
                pass

    def get_js_data(self, headers_text):
        pn = 1
        headers = get_headers(headers_text)
        while 1:
            try:
                link = self.link.replace("pn=1", "pn={}".format(pn))
                response = requests.get(link, headers=headers)
                sleep(5)
                result = response.text
                result = json.loads(result[6:-1])
                video_list = jsonpath.jsonpath(result, '$..archives')[0]
                print(len(video_list), pn)
                if len(video_list) == 0:
                    break
                for v in video_list:
                    video = UpVideo(
                        link="https://www.bilibili.com/video/av{}/".format(v.get("aid")),
                        up=self.name,
                        aid=v.get("aid"),
                        title=v.get("title"),
                        length=v.get("duration"),
                        pic=v.get("pic"),
                        state=0
                    )
                    save_result = video.save_to_mongodb(self.mdb)
                    if save_result == 9:
                        self.mdb.update({"aid": video.aid}, {"up": self.name})
                pass
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pn += 1
                pass
            finally:
                pass

    def down_video(self, count=10):
        for video in self.mdb.select(up=self.name, n=count):
            try:
                v_obj = UpVideo(video)
                if v_obj.state is not None and v_obj.state >= 1:
                    continue
                down_state = down_load(self.file_path, v_obj.link, name=str(v_obj.aid))
                if down_state == 0:
                    continue
                self.mdb.update({"aid": video.get("aid")}, {"state": 1})
                pass
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pass
            finally:
                pass

    def preview_list(self, count=100):
        for video in self.mdb.select(up=self.name, n=count):
            try:
                v_obj = UpVideo(video)
                if v_obj.state is None and v_obj.state != 1:
                    continue
                if v_obj.pic is None:
                    preview_result = preview(v_obj.aid, self.file_path, self.preview_path)
                else:
                    preview_result = ordinary_down_load("http:" + v_obj.pic,
                                                        "{}\\{}.jpg".format(self.preview_path, v_obj.aid))
                if preview_result:
                    self.mdb.update({"aid": video.get("aid")}, {"state": 2})
                pass
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pass
            finally:
                pass

    def __str__(self):
        return ""


# def preview_list(path):
#     try:
#         files = os.listdir(path)
#         for video in files:
#             preview(os.path.splitext(video)[0], path, "{}\\feng".format(path))
#             print(video)
#         pass
#     except Exception as e:
#         print("Error:{}".format(e))
#     else:
#         pass
#     finally:
#         pass


def de_watermark_list(up_user):
    files = os.listdir(up_user["file_path"])
    for video in files:
        try:
            video_name = os.path.splitext(video)[0]
            video_path = "{}\\{}.mp4".format(up_user["file_path"], video_name)
            image_path = "{}\\feng\\{}.jpg".format(up_user["file_path"], video_name)
            clear_path = "{}\\{}".format(up_user["clean_path"], File(video_path).name)
            if os.path.exists(clear_path):
                print("已去除水印！")
                continue
            if not os.path.exists(image_path):
                print("没有预览图")
                continue
            text = get_txt_img(image_path)
            if len(text) == 0:
                shutil.move(video_path, clear_path)
                continue
            for w in text:
                if up_user["watermark_words"] in w:
                    size = img_shape(image_path)
                    if size is not None:
                        de_watermark(video_path, size["width"] - up_user["watermark"]["w"] - 10,
                                     up_user["watermark"]["y"],
                                     up_user["watermark"]["w"], up_user["watermark"]["h"],
                                     out_path=up_user["clean_path"])
                    break
            # print(video_name, ":", text)
            sleep(5)
            pass
        except Exception as e:
            print("Error:{}".format(e))
        else:
            pass
        finally:
            pass


def get_headers(text):
    try:
        headers = {}
        for t in text.split("\n"):
            k = t.split(": ")
            headers[k[0]] = k[1]
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return headers
        pass
    finally:
        pass


if __name__ == '__main__':
    pass

    xiao_dan = {
        "name": "晓丹小仙女儿",
        "link": "https://api.bilibili.com/x/space/arc/search?mid=21648772&"
                "ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp",
        "file_path": r"D:\Anubis\Video\bilibili",
        "preview_path": r"D:\Anubis\Video\bilibili\feng",
        "clean_path": r"D:\Anubis\Video\bilibili\clear",
        "watermark_words": "晓丹小",
        "watermark": {"y": 20, "w": 430, "h": 100},
        "mdb": MongodbClient(db="SpiderData", table="bilibili", host="localhost")
    }
    # baoke_meng = {
    #     "name": "宝可梦",
    #     "link": [
    #         "https://api.bilibili.com/x/space/arc/search?mid=292703435&ps=30&tid=0&pn=2&keyword=&order=pubdate&jsonp=jsonp",
    #         ""],
    #     "file_path": r"D:\Anubis\Video\bilibili\yuan",
    #     "preview_path": r"D:\Anubis\Video\bilibili\feng",
    #     "clean_path": r"D:\Anubis\Video\bilibili\clear",
    #
    # }
    baoke_meng = BilibiliUp(
        name="宝可梦",
        link="https://api.bilibili.com/x/space/arc/search?mid=292703435&ps=30&tid=0&"
             "pn=1&keyword=&order=pubdate&jsonp=jsonp",
        file_path=r"D:\Anubis\Video\bilibili\yuan",
        preview_path=r"D:\Anubis\Video\bilibili\feng",
        clean_path=r"D:\Anubis\Video\bilibili\clear",
        mdb=MongodbClient(db="SpiderData", table="bilibili", host="localhost")
    )
    sss = """accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: finger=158939783; buvid3=25EAAFFA-208B-482A-9730-E51C080CAEB649027infoc; stardustvideo=1; sid=htigihgq; rpdid=|(umJJJRmll|0J'ullYl|Yllk; LIVE_BUVID=AUTO8415597013171326; fts=1562493994; stardustpgcv=0606; im_notify_type_446127665=0; INTVER=1; laboratory=1-1; DedeUserID=446127665; DedeUserID__ckMd5=6cd4ad1346cc8113; SESSDATA=0aa0d033%2C1608263596%2C1102c*61; bili_jct=bf3c3090f739518e260c071aa643131e; _uuid=9229A7BB-E31B-8DB2-CF1D-F014517A6BFD88968infoc; CURRENT_FNVAL=80; blackside_state=1; CURRENT_QUALITY=80; bsource=search_baidu; bp_video_offset_446127665=445617983836792180; PVID=2; bfe_id=393becc67cde8e85697ff111d724b3c8
referer: https://space.bilibili.com/
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
sec-fetch-dest: script
sec-fetch-mode: no-cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"""
    s_link = "https://api.bilibili.com/x/space/channel/video?mid=292703435&cid=152031&pn=1" \
             "&ps=30&order=0&jsonp=jsonp&callback=__jp6"
    # result = requests.get(link, headers=get_headers(sss)).text
    # print(json.loads(result[6:-1]))
    baoke_meng.link = s_link
    baoke_meng.name = "宋姝儿"
    baoke_meng.down_video()
    baoke_meng.preview_list()
