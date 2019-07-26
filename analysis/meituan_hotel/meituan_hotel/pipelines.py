# -*- coding: utf-8 -*-

import csv
import logging
import os
from datetime import datetime

from meituan_hotel.items import MeituanHotelItem


class CsvWriterPipeline(object):
    index: int = 0
    file = None
    writer: csv.DictWriter = None

    def open_spider(self, spider):

        base_path = os.path.abspath("../../dataSet/{date}/".format(
            date=datetime.now().strftime('%Y-%m-%d')))
        init_path(base_path)
        if spider.name in ['meituan_url_item','meituan_urls_item']:
            self.file = open(base_path + '/data_url.csv', 'w', encoding='utf-8',
                             newline='')
            self.writer = csv.DictWriter(self.file, ['url'])
        else:
            self.file = open(base_path + '/dataSet_item.csv', 'w',
                             encoding='utf-8',
                             newline='')
            self.writer = csv.DictWriter(self.file, MeituanHotelItem.fields)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()
        logging.info("文件将保存")

    def process_item(self, item, spider):
        self.index = self.index + 1
        logging.info("已成功抓取到：%s条数据", self.index)
        self.writer.writerow(item)
        return True


def init_path(file_path) -> None:
    is_exists: bool = os.path.exists(file_path)

    if not is_exists:
        logging.info("初始化创建目录:%s", file_path)
        os.makedirs(file_path)
