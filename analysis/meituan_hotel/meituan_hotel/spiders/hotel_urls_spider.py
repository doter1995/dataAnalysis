import logging
import time

from scrapy import Spider, Request
from selenium import webdriver

from meituan_hotel.items import MeituanHotelUrlItem


class hotal(Spider):
    name = "meituan_urls_item"
    types = ["舒适/三星", "高档/四星", "豪华/五星"]
    prices = ["100以下", "100-200元", "200-300元", "300-400元", "500以上"]
    select_search = ["经济型", "100以下"]
    index = 1
    pages = 1

    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('--headless')
        # chromeOptions.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)
        self.browser.set_window_size(1920, 1080)
        self.browser.set_page_load_timeout(60)

    def closed(self, spider):
        self.browser.close()
        logging.info("spider closed")

    def start_requests(self):
        url = "https://hotel.meituan.com/xian/"
        for x in self.types:
            self.select_search[0] = x
            for y in self.prices:
                self.select_search[1] = y
                yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.browser.find_element_by_link_text(self.select_search[0]).click()
        time.sleep(1)
        self.browser.find_element_by_link_text(self.select_search[1]).click()
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
                    pass
        if self.index < self.pages:
            next_page = self.find_css("ul.paginator li.current+li a")[0]
            time.sleep(2)
            self.index = int(next_page.text)
            next_page.click()
        else:
            self.index = self.index + 1

    def find_css(self, css):
        return self.browser.find_elements_by_css_selector(css)
