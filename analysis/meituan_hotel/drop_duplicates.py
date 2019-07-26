import os
from datetime import datetime
import logging
import pandas as pd


def drop_Url_duplicates(path):
    dataSet_url_path = os.path.abspath("../../dataSet/dataSet_url.csv")
    csv_data = pd.read_csv(path + '/data_url.csv')
    csv_data["id"] = csv_data["url"].map(lambda x: x.split("/")[3])
    csv_data = csv_data.drop_duplicates("id")
    csv_data.to_csv(path + '/data_url.csv', index=0, columns=["id", "url"])
    base_url_data = pd.read_csv(dataSet_url_path)
    base_url_data = pd.concat([base_url_data, csv_data]).drop_duplicates("id")
    base_url_data.to_csv(dataSet_url_path,
                         index=0,
                         columns=["id", "url"])


def get_need_url():
    dataSet_item_path = os.path.abspath("../../dataSet/dataSet_item.csv")
    dataSet_url_path = os.path.abspath("../../dataSet/dataSet_url.csv")
    url_data = pd.read_csv(dataSet_url_path)
    item_data = pd.read_csv(dataSet_item_path)
    url_data = url_data[~url_data.id.isin(item_data["id"])]
    url_data.to_csv(dataSet_url_path, index=0, columns=["id", "url"])


def url_duplicates():
    path = os.path.abspath("../../dataSet/{date}/".format(
        date=datetime.now().strftime('%Y-%m-%d')))
    drop_Url_duplicates(path)
    logging.info("删除重复url，并且将其更新到dataSet_url中")
    get_need_url()
    logging.info("更新当前需要的抓取的Url")
