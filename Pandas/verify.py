import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#date personale despre angajati

data = {
     "nume":['Camilia', 'Mihai', 'Oneac', 'Catalin'],
     "prenume":['Pipas', 'Negoita', 'Bodac', 'Rotaru'],
     "varsta":[31, 38, 28, 25],
     "sex":['Feminin', 'Masculin', 'Masculin', 'Masculin'],
     "departament":['Coordonator', 'Operator', 'Manager', 'Technician'],
     "oras":['Pecica', 'Santoma', 'Olar', 'Sicula']

}


df = pd.DataFrame({
    'name': ['John Smith', 'Sarah Chen', 'Mike Ross', 'Anna Lee', 'Tom Wilson'],
    'age': [25, 30, 22, 35, 28],
    'salary': [50000, 75000, 45000, 85000, 62000],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'experience': [2.5, 5.0, 1.5, 8.0, 4.0],
    'rating': [4.5, np.nan, 3.8, 4.2, np.nan],
    'is_manager': [False, True, False, True, False],
    'projects': [3, 5, 2, 4, 3]
})

df =pd.DataFrame(data)
print("=============Welcome=========")
#print(df) #Just use when u want
#print(df.head)  #Just use when u need
#print(df.iloc[0:2])# See just two raw.
print("========Filtering method========")

#Using boolean filter method.

# Get all employees older than 25
#older_employees = df[df['age'] > 25]

# Get IT department employees
#it_employees = df[df['department'] == 'IT']

# Direct boolean filtering
#managers = df[df['is_manager']] == 0

# Combining boolean conditions
#senior_managers = df[df['is_manager'] & (df['experience'] > 5)]
print("=======Using multiply condition======")
# Condition and or not.
# Get HR employees with salary > 70000
#hr_high_salary = df[(df['department'] == 'HR') & (df['salary'] > 70000)]

# Get employees either in IT or with age > 30
#it_or_older = df[(df['department'] == 'IT') | (df['age'] > 30)]
print("====Using isin() multiply value=====")
#Using isin() method.
# Get employees in specific departments
#selected_depts = df[df['department'].isin(['IT', 'Finance'])]

# Filter multiple values
selected_depts = ['IT', 'Finance']
tech_finance_employees = df[df['department'].isin(selected_depts)]

# Inverse selection (not in list)
other_depts = df[~df['department'].isin(selected_depts)]
print("=======Using querry method=====")
# Usin to compare data and filtering.
# Get employees with age between 25 and 30
#age_range = df.query('25 <= age <= 30')

print("====Using string filterin====")
#Using to filter string data.
# Get names starting with 'A'
#a_names = df[df['name'].str.startswith('A')]

# Contains specific text
contains_smith = df[df['name'].str.contains('Smith')]

# Case-insensitive search
contains_smith_any_case = df[df['name'].str.contains('smith', case=False)]

# Ends with specific text
ends_with_lee = df[df['name'].str.endswith('Lee')]

# String length
long_names = df[df['name'].str.len() > 8]

