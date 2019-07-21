from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
import time


class MeituanHotelDownloaderMiddleware(object):

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        print("请求地址:"+request.url)
        if spider.name == 'meituan':
            try:
                spider.browser.get(request.url)
            except TimeoutException as e:
                print('超时')
                spider.browser.execute_script('window.stop()')
            time.sleep(2)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)
        return None
