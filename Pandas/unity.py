import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Date destpre angajati.
data = {
    "nume":['Florian', 'Alexandra', 'Doru', 'Stefan',],
    "varsta ":[32, 45, 23,28],
    "sex":['Masculin', 'Feminin', 'Masculin', 'Masculin'],
    "departament":['Inginer', 'Consultant', 'Financiar', 'Manager'],
    "oras":['Curtici', 'Cicir', 'Santana', 'Horea']


}



#Vizualizarea datelor din tabel.
df = pd.DataFrame(data)
print(df)
print("===========================")
print(df.loc[2])
print("============================")
print(df.loc[[0, 1]])
print("=============================")
print(df.to_string )
print("------------------------------")
print(df.head)

