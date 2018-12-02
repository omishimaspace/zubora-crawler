# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

from .items import REQUIRED


class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        for col in REQUIRED:
            if col not in item:
                raise DropItem(f'{col} is required.')
        return item


class ZuboraCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
