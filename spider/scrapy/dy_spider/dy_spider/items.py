# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DySpiderItem(scrapy.Item):
    id = scrapy.Field()
    text = scrapy.Field()
    videos = scrapy.Field()
    images = scrapy.Field()
    comments = scrapy.Field()
    down = scrapy.Field()
    update = scrapy.Field()
    down_comment = scrapy.Field()
    pass


if __name__ == '__main__':
    ss = "id,text,videos,images,comments,down,update,down_comment"
    for i in ss.split(","):
        print(i + "= scrapy.Field()")
