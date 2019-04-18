# -*- coding: utf-8 -*-
import scrapy
from renrenmovie.items import RenrenmovieItem
import re
class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['www.zimuzu.io']
    start_urls = ['http://www.zimuzu.io/resourcelist/?page=1&channel=&area=&category=&year=&tvstation=&sort=']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='resource-showlist has-point']//li")
        for i_item in movie_list:
            renren_item = RenrenmovieItem()
            num = i_item.xpath(".//div[@class='fl-img']/a//em/text()").extract()\
                  + i_item.xpath(".//div[@class='fl-img']/a//span/text()").extract()
            renren_item['star'] ="".join(num)
            renren_item['tag'] = i_item.xpath(".//div[@class='fl-info']//strong[@class='tag tv']/text()")\
                .extract_first()
            renren_item['movie_name'] = i_item.xpath(".//div[@class='fl-info']//a/text()").extract_first()
            favourite_content = i_item.xpath(".//div[@class='fl-info']//dd/p[1]/text()").extract()
            for test in  favourite_content:
                test1 = test.split()[0]
                if(test1 == '【类型】'):
                    type = i_item.xpath(".//div[@class='fl-info']//dd/p[1]/text()").extract()
                    for i_type in type:
                        renren_item['type'] = i_type.split()[1]
                    favourite = i_item.xpath(".//div[@class='fl-info']//dd/p[2]/text()").extract()
                    for i_favourite in favourite:
                        renren_item['favourite'] = re.sub("\D", "", i_favourite.split('|')[1])
                else:
                    type = i_item.xpath(".//div[@class='fl-info']//dd/p[2]/text()").extract()
                    for i_type in type:
                        renren_item['type'] = i_type.split()[1]
                    favourite = i_item.xpath(".//div[@class='fl-info']//dd/p[3]/text()").extract()
                    for i_favourite in favourite:
                        renren_item['favourite'] = re.sub("\D", "", i_favourite.split('|')[1])
            renren_item['ranking'] = i_item.xpath(".//div[@class='fl-info']//dd//font[@class='f1']/text()")\
                .extract_first()
            yield renren_item
        #对剩下的网页进行爬取
        for i in range(2,711):
            num = '%d'%i
            yield scrapy.Request("http://www.zimuzu.io/resourcelist/?page=" + num
                                 + "&channel=&area=&category=&year=&tvstation=&sort=", callback=self.parse)
