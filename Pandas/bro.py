import pandas as pd

data = {
    "produse":['margarina', 'toffu', 'mustar'],
    "pret":[4.50, 6.78, 9.20],
    "cantitate":[2, 4, 2],
    "LOT":['L64P', 'L410', 'L1P09']

 }

df = pd.DataFrame(data)
print(df)
print(df. loc[ 2])
print(df.loc[[0, 1]])
