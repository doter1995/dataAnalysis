import pandas as pd

csv_data = pd.read_csv('data_url.csv')

csv_data['id'] = csv_data['url'].map(lambda x: x[26:].split("/")[0])

print(csv_data.duplicated("id"))

csv_data = csv_data.drop_duplicates("id")
csv_data.to_csv('data_url.csv', index=0)
