import logging
import os
import random

import pandas as pd


def get_random_proxy():
    """随机从文件中读取proxy"""
    base_path = os.path.abspath("./../dataSet/proxies.csv")
    data_set = pd.read_csv(base_path)
    proxy = random.choice(data_set["url"]).strip()
    logging.info("重新抽取ip代理:%s", proxy)
    return proxy
