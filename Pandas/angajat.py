import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data autonom employee.

data = {
    'name': ['Maria', 'Petre', 'Emanuil', 'Alexandru', 'Cornel'],
    'age':[24, 31, 26, 29, 34 ],
    'departament':['HR', 'Inginer', 'Finance', 'Consultan', 'CEO'],
    'salary':[ 3.500, 4.800, 4.200, 3.700, 8.900],
    'gender':['Female', 'Male', 'Male', 'Male', 'Male']

}
#Create DataFrame

df = pd.DataFrame(data)

#1. Print Basic Data Exploration
print("Basic Data info:")
print(df)
print("========================")
print(df.head())
print("=========================================")
print(df.info())
print(df.to_string())
print("===============================")
print("\nAccessing columns: ")
print("--------------------------------")
print(df['name'])#Acces name control.
print(df[['gender', 'age']])#Accesing multiline column.

