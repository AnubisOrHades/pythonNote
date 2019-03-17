import requests
from Example.my_get import down_load
import json

path = r"D:\Anubis\SpiderData\哔哩哔哩\3次元"


class MV:
    def __init__(self, senddate=None, rank_offset=None, tag=None, duration=None, id=None, rank_score=None,
                 badgepay=None, pubdate=None, title=None, review=None, mid=None, is_union_video=None, rank_index=None,
                 type=None, arcrank=None, play=None, pic=None, description=None, video_review=None, is_pay=None,
                 favorites=None, arcurl=None, author=None, path=None):
        self.senddate = senddate
        self.rank_offset = rank_offset
        self.tag = tag
        self.duration = duration
        self.id = id
        self.rank_score = rank_score
        self.badgepay = badgepay
        self.pubdate = pubdate
        self.title = title
        self.review = review
        self.mid = mid
        self.is_union_video = is_union_video
        self.rank_index = rank_index
        self.type = type
        self.arcrank = arcrank
        self.play = play
        self.pic = pic
        self.description = description
        self.video_review = video_review
        self.is_pay = is_pay
        self.favorites = favorites
        self.arcurl = arcurl
        self.author = author
        self.path = path

    def save(self):
        try:
            down_load(self.path, self.arcurl)
        except Exception as e:
            with open("error.text", "a")as f:
                data = "Error:{}\n\nErrorUrl:{}".format(e, self.arcurl)
                f.write(data)


def get_url(url):
    html = requests.get(url)
    data = html.content
    data = str(data, 'utf-8')
    data = json.loads(data[37:-1])
    # for i, v in data.items():
    #     print(i,"\t",v)
    result = data["result"]
    for r in result:
        mv = MV()
        mv.senddate = r.get('senddate')
        mv.rank_offset = r.get('rank_offset')
        mv.tag = r.get('tag')
        mv.duration = r.get('duration')
        mv.id = r.get('id')
        mv.rank_score = r.get('rank_score')
        mv.badgepay = r.get('badgepay')
        mv.pubdate = r.get('pubdate')
        mv.title = r.get('title')
        mv.review = r.get('review')
        mv.mid = r.get('mid')
        mv.is_union_video = r.get('is_union_video')
        mv.rank_index = r.get('rank_index')
        mv.type = r.get('type')
        mv.arcrank = r.get('arcrank')
        mv.play = r.get('play')
        mv.pic = r.get('pic')
        mv.description = r.get('description')
        mv.video_review = r.get('video_review')
        mv.is_pay = r.get('is_pay')
        mv.favorites = r.get('favorites')
        mv.arcurl = r.get('arcurl')
        mv.author = r.get('author')
        mv.path = path
        print(mv.arcurl)
        mv.save()


if __name__ == '__main__':
    get_url(
        "https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_9367045062332786&main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=154&page=1&pagesize=20&jsonp=jsonp&time_from=20190307&time_to=20190314&_=1552552839641")
    pass
