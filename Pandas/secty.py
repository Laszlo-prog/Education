import pandas as pd
import numpy as np

# Create sample dataset
data = {
    'name': ['John', 'Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace'],
    'age': [25, 30, 35, 28, 42, 31, 29, 33],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [60000, 55000, 75000, 65000, 80000, 62000, 70000, 58000],
    'experience': [2, 5, 8, 3, 12, 4, 6, 7],
    'performance_score': [4.5, 4.2, 4.8, 3.9, 4.6, 4.1, 4.3, 4.4]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# 1. Basic Filtering with Single Condition
print("1. Employees in IT department:")
it_employees = df[df['department'] == 'IT']
print(it_employees)
print("\n" + "="*50 + "\n")

# 2. Multiple Conditions using & (and)
print("2. Employees in IT with salary > 65000:")
it_high_salary = df[(df['department'] == 'IT') & (df['salary'] > 65000)]
print(it_high_salary)
print("\n" + "="*50 + "\n")

# 3. Multiple Conditions using | (or)
print("3. Employees in either IT or HR:")
it_or_hr = df[(df['department'] == 'IT') | (df['department'] == 'HR')]
print(it_or_hr)
print("\n" + "="*50 + "\n")

# 4. Filtering with isin()
print("4. Employees in specific departments using isin():")
selected_dept = df[df['department'].isin(['IT', 'Finance'])]
print(selected_dept)
print("\n" + "="*50 + "\n")

# 5. Filtering with string methods
print("5. Names starting with 'J' or 'A':")
j_or_a_names = df[df['name'].str.startswith(('J', 'A'))]
print(j_or_a_names)
print("\n" + "="*50 + "\n")

# 6. Numeric Range Filtering
print("6. Employees aged between 30 and 35:")
age_range = df[(df['age'] >= 30) & (df['age'] <= 35)]
print(age_range)
print("\n" + "="*50 + "\n")

# 7. Complex Conditions
print("7. Complex filtering: IT/HR employees with high performance:")
complex_filter = df[
    ((df['department'].isin(['IT', 'HR'])) & 
     (df['performance_score'] > 4.2) & 
     (df['salary'] > 60000))
]
print(complex_filter)
print("\n" + "="*50 + "\n")

# 8. Using query() method
print("8. Using query() method:")
query_result = df.query("age < 30 and salary > 55000")
print(query_result)
print("\n" + "="*50 + "\n")

# 9. Filtering with null values
# Add some null values first
df.loc[0, 'performance_score'] = np.nan
print("9. Filtering null values:")
null_scores = df[df['performance_score'].isnull()]
non_null_scores = df[df['performance_score'].notnull()]
print("Rows with null scores:")
print(null_scores)
print("\nRows with non-null scores:")
print(non_null_scores)
print("\n" + "="*50 + "\n")

# 10. Using iloc and loc
print("10. Using iloc and loc:")
print("\nFirst 3 rows using iloc:")
print(df.iloc[0:3])
print("\nFiltering with loc using index and conditions:")
print(df.loc[df['salary'] > 70000, ['name', 'salary', 'department']])