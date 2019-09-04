import os
from datetime import datetime
import logging
import pandas as pd


def drop_Url_duplicates(path,city):
    dataSet_url_path = os.path.abspath("./../dataSet/dataSet_url_{city}.csv".format(city=city))
    csv_data = pd.read_csv(path + '/data_url_{city}.csv'.format(city=city))
    csv_data["id"] = csv_data["url"].map(lambda x: x.split("/")[3])
    csv_data = csv_data.drop_duplicates("id")
    csv_data.to_csv(path + '/data_url_{city}.csv'.format(city=city), index=0, columns=["id", "url"])
    base_url_data = pd.read_csv(dataSet_url_path)
    base_url_data = pd.concat([base_url_data, csv_data]).drop_duplicates("id")
    base_url_data.to_csv(dataSet_url_path,
                         index=0,
                         columns=["id", "url"])


def get_need_url(city):
    dataSet_item_path = os.path.abspath("./../dataSet/dataSet_item_{city}.csv".format(city=city))
    dataSet_url_path = os.path.abspath("./../dataSet/dataSet_url_{city}.csv".format(city=city))
    url_data = pd.read_csv(dataSet_url_path)
    item_data = pd.read_csv(dataSet_item_path)
    url_data = url_data[~url_data.id.isin(item_data["id"])]
    url_data.to_csv(dataSet_url_path, index=0, columns=["id", "url"])


def url_duplicates(city):
    path = os.path.abspath("./../dataSet/{date}/".format(
        date=datetime.now().strftime('%Y-%m-%d')))
    drop_Url_duplicates(path,city)
    logging.info("删除重复url，并且将其更新到dataSet_url中")
    get_need_url(city)
    logging.info("更新当前需要的抓取的Url")


def merage_item_data(city):
    dataSet_item_path = os.path.abspath("./../dataSet/{date}/dataSet_item_{city}.csv".format(
        date=datetime.now().strftime('%Y-%m-%d'),city=city))
    base_item_path = os.path.abspath("./../dataSet/dataSet_item_{city}.csv".format(city=city))
    item_data = pd.read_csv(dataSet_item_path)
    base_item_data = pd.read_csv(base_item_path)
    base_item_data = pd.concat([base_item_data, item_data]).drop_duplicates("id")
    base_item_data.to_csv(base_item_path, index=0)
