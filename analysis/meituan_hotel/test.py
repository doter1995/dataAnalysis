import os
from datetime import datetime
import logging
import pandas as pd


def getIndex(x):
    if x == "舒适型" or x == "名宿":
        return 2
    elif x == "豪华型" or x == "五星级":
        return 3
    return 1


def merage_item_data():
    base_item_path = os.path.abspath("./../dataSet/dataSet_item.csv")
    base_item_data = pd.read_csv(base_item_path)
    base_item_data["type"] = base_item_data["type"].map(getIndex)
    base_item_data.to_csv(os.path.abspath(
        "./../dataSet/dataSet_item2.csv"), index=0)


merage_item_data()
