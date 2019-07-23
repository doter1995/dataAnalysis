from scrapy import Spider, Request
from selenium import webdriver
from meituan_hotel.items import MeituanHotelUrlItem
import logging

class hotal(Spider):
  name = "meituan_url_item"

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
    url = "https://hotel.meituan.com/xian/pn"
    i = 0
    while i < 76:
      i = i + 1
      yield Request(url + str(i), callback=self.parse)

  def parse(self, response):
    item = MeituanHotelUrlItem()
    url_list = response.xpath(
        "//article[@class='poi-item']/div[@class='info-wrapper']/h3/a[@class='poi-title']/@href").extract()
    for url in url_list:
      item["url"] = url
      yield item
