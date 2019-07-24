import os
from datetime import datetime

import pandas as pd


def drop_Url_duplicates(path):
    csv_data = pd.read_csv(path + '/data_url.csv')
    csv_data["id"] = csv_data["url"].map(lambda x: x.split("/")[3])
    csv_data = csv_data.drop_duplicates("id")
    csv_data.to_csv(path + '/data_url.csv', index=0, columns=["id", "url"])


path = os.path.abspath("../../dataSet/{date}/".format(
    date=datetime.now().strftime('%Y-%m-%d')))
drop_Url_duplicates(path)
