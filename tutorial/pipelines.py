# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymysql


class DuplicatesPipeline(object):
    def __init__(self):
        self.data = set()

    def process_item(self, item, spider):
        if item['url'] in self.data:
            raise DropItem("Duplicate item found")
        else:
            self.data.add(item['url'])
            return item


class SqlPipeline(object):
    def __init__(self):
        self.coon = pymysql.connect(host='139.224.134.103', port=3306, user='xiangchen', passwd='Pl1996317', db='test', charset='utf8')
        self.cur = self.coon.cursor()

    def process_item(self, item, spider):
        sql = "insert ignore into car_list values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cur.execute(sql, list(item.values()))
        self.coon.commit()
        return item

    def spider_closed(self, spider):
        self.cur.close()
        self.coon.close()
