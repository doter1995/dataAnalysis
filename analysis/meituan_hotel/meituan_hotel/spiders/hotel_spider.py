from scrapy import Spider, Request
from selenium import webdriver
from meituan_hotel.items import MeituanHotelItem
import re


class hotal(Spider):

    name = "meituan"

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(60)

    def closed(self, spider):
        pass
        self.browser.close()
        print("spider closed")

    def start_requests(self):
        url = "https://hotel.meituan.com/xian/pn"
        i = 1
        while i < 76:
            i = i+1
            yield Request(url+str(i), callback=self.parse)

    def parse(self, response):
        print('爬取最终数据...')
        url_list = response.xpath(
            "//article[@class='poi-item']/div[@class='info-wrapper']/h3/a[@class='poi-title']/@href").extract()
        for url in url_list:
            yield Request(url, callback=self.parse_hotel)

    def parse_hotel(self, response):
        item = MeituanHotelItem()
        item["id"] = self._fromartId(response.url)
        item['name'] = response.xpath(
            "//div[@class='poi-header']/div/div/span/text()")[0].extract()
        item['address'] = response.xpath(
            "//div[@class='poi-header']/div/div/span/text()")[1].extract()
        item["latlng"] = self._fromartLatlng(response.xpath(
            "//div[@class='map-display']/img/@src")[0].extract())
        # response.xpath("//ul[@class='deal-table']/span/li")
        yield item

    def _fromartLatlng(self, url):
        return url[url.rfind("|")+1:]

    def _fromartId(self, url):
        return url[url.rfind(".com/")+5:].split("/")[0]
