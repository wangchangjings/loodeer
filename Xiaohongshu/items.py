# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohongshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cover = scrapy.Field()
    article_url = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    author = scrapy.Field()
    avatar = scrapy.Field()
    likes = scrapy.Field()
    # pass
