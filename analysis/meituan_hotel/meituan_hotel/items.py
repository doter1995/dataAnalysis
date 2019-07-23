# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanHotelItem(scrapy.Item):
  id = scrapy.Field()
  name = scrapy.Field()
  address = scrapy.Field()
  latlng = scrapy.Field()
  type = scrapy.Field()
  score = scrapy.Field()
  tel = scrapy.Field()
  info = scrapy.Field()


class MeituanHotelUrlItem(scrapy.Item):
  url = scrapy.Field()
