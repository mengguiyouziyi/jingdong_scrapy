# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

class MongodbPipeline(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        dbname=settings['MONGODB_DBNAME']#数据库名
        client=pymongo.MongoClient(host=host,port=port)
        tdb=client[dbname]
        self.port=tdb[settings['MONGODB_COLECNAME']]#表名
    def process_item(self, item, spider):
        agentinfo=dict(item)
        print('agentinfo----' + agentinfo)
        self.port.insert(agentinfo)
        print('=============')
        return item



class JingdongPipeline(object):
    def process_item(self, item, spider):
        return item
