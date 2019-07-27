import logging
import time

from scrapy import Spider, Request
from selenium import webdriver

from meituan_hotel.items import MeituanHotelUrlItem


class hotal(Spider):
    name = "meituan_urls_item"
    index = 1
    pages = 1

    def __init__(self, city=None, sprices=None, stype=None, *args, **kwargs):
        self.city = city
        self.sprices = sprices
        self.stype = stype
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('--headless')
        # chromeOptions.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)
        self.browser.set_window_size(1420, 1080)
        self.browser.set_page_load_timeout(60)

    def closed(self, spider):
        self.browser.close()
        logging.info("spider closed")

    def start_requests(self):
        url = "https://hotel.meituan.com/{city}/".format(city=self.city)
        yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.browser.find_element_by_link_text(self.stype).click()
        time.sleep(1)
        self.browser.find_element_by_link_text(self.sprices).click()
        time.sleep(2)
        link_pages = self.find_css("li.page-link")
        self.pages = 1 if len(link_pages) == 0 else int(link_pages[-1].text)
        while self.index <= self.pages:
            time.sleep(2)
            url_list = self.find_css("article.poi-item a.poi-title")
            for url in url_list:
                try:
                    item = MeituanHotelUrlItem()
                    item["url"] = url.get_attribute("href")
                    yield item
                except:
                    yield item

            if self.index < self.pages:
                next_page = self.find_css("ul.paginator li.current+li a")[0]
                time.sleep(2)
                self.index = int(next_page.text)
                next_page.click()
            else:
                self.index = self.index + 1

    def find_css(self, css):
        return self.browser.find_elements_by_css_selector(css)
