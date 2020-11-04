from time import sleep
import os
import shutil

import requests

from db.MongoDB.pm import *
from tools.down_load.my_get import down_load
from tools.video import preview, de_watermark
from tools.image import get_txt_img, img_shape
from tools.file import File

"""
MongoDB state:
    1:已下载；2：已生成预览图（第一帧）；3已清除水印；
"""


def get_data(link, mongodb, up_name=None):
    pn = 1
    while 1:
        try:
            response = requests.get(link.format(pn))
            result = response.json()["data"]["list"]["vlist"]
            if len(result) == 0:
                break
            code = '{}.save{}'.format(mongodb, tuple(
                {"link": "https://www.bilibili.com/video/av{}/".format(l.get("aid")), "up": up_name} for l in result))
            eval(code)
            pass
        except Exception as e:
            print("Error:{}".format(e))
        else:
            pn += 1
            pass
        finally:
            sleep(5)
            pass


def down_video(down_load_path, mongodb):
    d = mongodb.select(n=None, up="晓丹小仙女儿")
    try:
        for s in d:
            if s.get("state") == 1:
                continue
            try:
                down_load(down_load_path, s.get("link"))
                mongodb.update({"link": s.get("link")}, {"state": 1})
                print(s.get("link"))
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pass
            finally:
                pass
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


def preview_list(path):
    try:
        files = os.listdir(path)
        for video in files:
            # video_path = os.path.join(path, video)
            #
            # img_path="{}\\feng\\{}.png".format(path,os.path.splitext(video)[0])
            preview(os.path.splitext(video)[0], path, "{}\\feng".format(path))
            print(video)
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


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
    de_watermark_list(xiao_dan)
