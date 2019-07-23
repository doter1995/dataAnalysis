# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from meituan_hotel.items import MeituanHotelItem
import csv
import logging


class CsvWriterPipeline(object):
  index = 0;

  def open_spider(self, spider):
    if spider.name == 'meituan_url_item':
      self.file = open('data_url.csv', 'w', encoding='utf-8', newline='')
      self.writer = csv.DictWriter(self.file, ['url'])
    else:
      self.file = open('dataSet_item.csv', 'w', encoding='utf-8', newline='')
      self.writer = csv.DictWriter(self.file, MeituanHotelItem.fields)
    self.writer.writeheader()

  def close_spider(self, spider):
    self.file.close()

  def process_item(self, item, spider):
    self.index = self.index + 1
    logging.info("已成功抓取到：" + str(self.index) + "条数据")
    self.writer.writerow(item)
    return True
