# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RenrenmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    star = scrapy.Field()
    tag = scrapy.Field()
    movie_name = scrapy.Field()
    describe = scrapy.Field()
    type = scrapy.Field()
    favourite = scrapy.Field()
    ranking = scrapy.Field()

