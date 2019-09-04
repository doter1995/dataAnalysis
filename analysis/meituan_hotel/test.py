import os
from datetime import datetime
import logging
import pandas as pd


def merage_item_data():
    base_item_path = os.path.abspath("./../dataSet/dataSet_item.csv")
    base_item_data = pd.read_csv(base_item_path)
    base_item_data["latlng"] = base_item_data["latlng"].map(lambda x:x.split(",")[1]+","+x.split(",")[0])
    base_item_data.to_csv(os.path.abspath(
        "./../dataSet/dataSet_item2.csv"), index=0)


merage_item_data()
