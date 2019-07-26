import logging
import time

from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

from meituan_hotel.proxy import get_random_proxy


class MeituanHotelDownloaderMiddleware(object):
    proxy = get_random_proxy()
    i = 0

    def process_request(self, request, spider):
        self.set_proxy()
        request.meta['proxy'] = self.proxy
        if spider.name == 'meituan_url_item':
            return self.request_url(request, spider)
        elif spider.name == 'meituan_hotel_item':
            return self.request_item(request, spider)
        elif spider.name == 'meituan_urls_item':
            return self.request_urls(request, spider)
        return None

    def set_proxy(self):
        if self.i == 0:
            self.random_proxy()
        self.i = (self.i + 1) % 5

    def random_proxy(self):
        self.proxy = get_random_proxy()

    def request_item(self, request, spider):
        try:
            spider.browser.delete_all_cookies()
            spider.browser.get(request.url)
            wait = WebDriverWait(spider.browser, 10)
            wait.until(
                Ec.presence_of_element_located((By.CLASS_NAME, "poi-header")))
        except TimeoutException as e:
            self.proxy = get_random_proxy()
            logging.warning("time out:===============")
            logging.warning("proxy:" + self.proxy)
            logging.warning("request url:" + request.url)
            logging.warning("time out:===============")
            spider.browser.execute_script('window.stop()')
        time.sleep(2)
        return HtmlResponse(url=spider.browser.current_url,
                            body=spider.browser.page_source,
                            encoding="utf-8", request=request)

    def request_url(self, request, spider):
        try:
            spider.browser.delete_all_cookies()
            spider.browser.get(request.url)
            wait = WebDriverWait(spider.browser, 10)
            wait.until(
                Ec.presence_of_element_located((By.CLASS_NAME, "poi-results")))
        except TimeoutException as e:
            logging.warning("time out:===============")
            logging.warning("proxy:" + self.proxy)
            logging.warning("request url:" + request.url)
            logging.warning("time out:===============")
            self.proxy = get_random_proxy()
            spider.browser.execute_script('window.stop()')
        if '很抱歉,暂时没有找到符合您条件的酒店' in spider.browser.page_source:
            self.random_Proxy()
            logging.error("**找到符合您条件的酒店**")
            logging.error("ip代理重新更换为")
            logging.error("proxy:" + self.proxy)
        time.sleep(2)
        return HtmlResponse(url=spider.browser.current_url,
                            body=spider.browser.page_source,
                            encoding="utf-8", request=request)

    def request_urls(self, request, spider):
        try:
            spider.browser.delete_all_cookies()
            spider.browser.get(request.url)
            wait = WebDriverWait(spider.browser, 10)
            wait.until(
                Ec.presence_of_element_located((By.CLASS_NAME, "poi-results")))
        except TimeoutException as e:
            logging.warning("time out:===============")
            logging.warning("proxy:" + self.proxy)
            logging.warning("request url:" + request.url)
            logging.warning("time out:===============")
            self.proxy = get_random_proxy()
            spider.browser.execute_script('window.stop()')
        if '很抱歉,暂时没有找到符合您条件的酒店' in spider.browser.page_source:
            logging.error("**找到符合您条件的酒店**")
            logging.error("ip代理重新更换为")
            logging.error("proxy:" + self.proxy)
        time.sleep(2)
        self.random_proxy()
        return HtmlResponse(url=spider.browser.current_url,
                            body=spider.browser.page_source,
                            encoding="utf-8", request=request)
