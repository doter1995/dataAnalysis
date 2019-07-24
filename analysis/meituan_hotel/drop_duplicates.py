import pandas as pd

csv_data = pd.read_csv('dataSet_item.csv')
csv_data = csv_data.drop_duplicates("id")
csv_data.to_csv('dataSet_item1.csv', index=0)
