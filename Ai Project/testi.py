import pandas as pd

data = {
    "name":['Laszlo', 'Balint', 'Foro'],
    "lastname":['Cornel', 'Avram', 'Mirel']

 }

df = pd.DataFrame(data)
print(df)
print(df. loc[ 2])
print(df.loc[[0, 1]])

