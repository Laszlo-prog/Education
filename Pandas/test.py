

import pandas as pd


df = pd.read_csv('worker.csv')

print(df.to_string())
print(df.filter(items=['Name', 'Age']))