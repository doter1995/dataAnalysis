import os
from datetime import datetime
import logging
import pandas as pd

def getCreateYear(item):
    items = []
    if isinstance(item, str) :
        items = item.split(",")

    if len(items) > 1:
        return int(items[1].replace("年开业", ""))
    return 0

def getUpdateYear(item):
    items = []
    if isinstance(item, str) :
        items = item.split(",")

    if len(items) > 1:
        return int(items[0].replace("年装修", ""))
    return 0

def translate(city):
    dataSet_url_path = os.path.abspath("./../dataSet/dataSet_item_{city}.csv".format(city=city))
    dataSet = pd.read_csv(dataSet_url_path)
    dataSet["create_year"] = dataSet["info"].map(getCreateYear)
    dataSet["update_year"] = dataSet["info"].map(getUpdateYear)
    del dataSet['info']
    dataSet.to_csv(os.path.abspath("./../dataSet/dataSet_item_{city}1.csv".format(city=city)))

translate("xian");