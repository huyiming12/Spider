# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from renrenmovie import settings

class RenrenmoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into renrenmovie(ranking,
                movie_name,tag,type,favourite,star)
                value(%s,%s,%s,%s,%s,%s)""",
                (item['ranking'],
                 item['movie_name'],
                 item['tag'],
                 item['type'],
                 item['favourite'],
                 item['star']))
            self.connect.commit()
        except Exception as err:
            print("重复插入了==》错误信息：" + str(err))

        return item
