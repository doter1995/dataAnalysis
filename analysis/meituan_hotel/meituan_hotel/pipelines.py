# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class CsvWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('data.csv', 'w', encoding='utf-8', newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        writer = csv.DictWriter(self.file, item.keys())
        writer.writerows([item])
        return True
