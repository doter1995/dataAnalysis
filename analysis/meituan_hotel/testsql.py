import pandas as pd
import pymysql
a = pymysql.connect(host='10.205.11.225', port=3306, user='time_card',
                    passwd='time_card@password', db='timecard', use_unicode=True, charset="utf8")

sql = "select * from time_card "

data = pd.read_sql(sql, con=a)
print(data)

a.close()
data = data.drop_duplicates(["staff_id_no", "access_time"])
data.to_csv("./data1.csv")
