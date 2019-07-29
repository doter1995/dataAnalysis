import logging
import os

from drop_duplicates import url_duplicates,merage_item_data

os.system("scrapy crawl huanqiu_finance")

# execute("scrapy crawl meituan_url_item".split())

# url_duplicates()


types = ["舒适/三星", "高档/四星", "豪华/五星"]
prices = ["100以下", "100-200元", "200-300元", "300-400元", "500以上"]

cmd_templete = "scrapy crawl meituan_urls_item -a stype={stype} -a sprices={sprices} -a city={city}"
log_templete = "---{city}----{stype}---{sprices}"



def crawl_hotel_meituan(city):
    for stype in types:
        for sprices in prices:
            cmd = cmd_templete.format(stype=stype, sprices=sprices, city=city)
            print("准备爬虫")
            print(log_templete.format(stype=stype, sprices=sprices,
                                             city=city))
            os.system(cmd)
            print("爬取完毕")
            print(log_templete.format(stype=stype, sprices=sprices,
                                            city=city))
            url_duplicates()
            print("merge data finish")


crawl_hotel_meituan("xian")

os.system("scrapy crawl meituan_hotel_item")

merage_item_data()