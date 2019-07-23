from scrapy import Spider, Request
from selenium import webdriver
from meituan_hotel.items import MeituanHotelItem
import pandas as pd
import logging

class hotal(Spider):
  name = "meituan_hotel_item"

  def __init__(self):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')
    self.browser = webdriver.Chrome(chrome_options=chromeOptions)
    self.browser.set_page_load_timeout(60)

  def closed(self, spider):
    self.browser.close()
    logging.info("spider closed")

  def start_requests(self):
    csv_data = pd.read_csv('data_url.csv')
    i = 0
    while i < csv_data["url"].size:
      yield Request(str(csv_data["url"][i]), callback=self.parse)
      i = i + 1

  def parse(self, response):
    logging.info("parse:"+response.url)
    item = MeituanHotelItem()
    item["id"] = self.fromartId(response.url)
    item['name'] = response.xpath(
        "//div[@class='poi-header']/div/div/span/text()")[0].extract()
    item['address'] = response.xpath(
        "//div[@class='poi-header']/div/div/span/text()")[1].extract()
    item["latlng"] = self.fromartLatlng(response.xpath(
        "//div[@class='map-display']/img/@src")[0].extract())
    item["type"]  = response.xpath(
        "//div[@class='poi-header']/div/div/div/span/text()")[0].extract()
    item['score'] = response.xpath(
        "//div[@class='rate-header']//em[@class='score-color']/text()")[0].extract()
    item["tel"] = response.xpath("//div[@class='poi-display']/ul/li[2]/div[2]/text()").extract()
    item["info"] = ",".join(response.xpath("//div[@class='poi-display']/ul/li[2]/div[1]/span/text()").extract())
    # response.xpath("//ul[@class='deal-table']/span/li")
    yield item

  def fromartLatlng(self, url):
    return url[url.rfind("|") + 1:]

  def fromartId(self, url):
    return url[url.rfind(".com/") + 5:].split("/")[0]
