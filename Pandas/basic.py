import pandas as pd
import numpy as np

# 1. Creating DataFrames
print("1. CREATING DATAFRAMES")
print("-" * 50)

# From dictionary
data_dict = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, 22, 35, 32],
    'city': ['New York', 'Paris', 'London', 'Tokyo']
}
df1 = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(df1)
print("\n")

# From list of lists
data_list = [
    ['John', 28, 'New York'],
    ['Anna', 22, 'Paris'],
    ['Peter', 35, 'London'],
    ['Linda', 32, 'Tokyo']
]
df2 = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print("DataFrame from list of lists:")
print(df2)
print("\n")

# 2. Basic Information
print("2. BASIC INFORMATION")
print("-" * 50)
print("\nDataFrame Info:")
print(df1.info())
print("\nDataFrame Description:")
print(df1.describe())
print("\nDataFrame Shape:", df1.shape)
print("\nColumn Names:", df1.columns.tolist())
print("\nData Types:")
print(df1.dtypes)
print("\n")

# 3. Basic Operations
print("3. BASIC OPERATIONS")
print("-" * 50)

# Accessing columns
print("First column (name):")
print(df1['name'])
print("\nMultiple columns:")
print(df1[['name', 'age']])

# Accessing rows
print("\nFirst row:")
print(df1.iloc[0])
print("\nFirst 2 rows:")
print(df1.head(2))
print("\nLast 2 rows:")
print(df1.tail(2))

# 4. Adding and Modifying Data
print("\n4. ADDING AND MODIFYING DATA")
print("-" * 50)

# Add new column
df1['country_code'] = ['US', 'FR', 'UK', 'JP']
print("\nAdded new column:")
print(df1)

# Modify existing column
df1['age'] = df1['age'] + 1
print("\nModified ages (added 1 year):")
print(df1)

# Add new row
new_row = pd.DataFrame({
    'name': ['Mike'],
    'age': [45],
    'city': ['Berlin'],
    'country_code': ['DE']
})
df1 = pd.concat([df1, new_row], ignore_index=True)
print("\nAdded new row:")
print(df1)

# 5. Basic Data Cleaning
print("\n5. BASIC DATA CLEANING")
print("-" * 50)

# Create DataFrame with missing values
df_messy = pd.DataFrame({
    'name': ['John', 'Anna', None, 'Linda'],
    'age': [28, np.nan, 35, 32],
    'city': ['New York', 'Paris', 'London', None]
})

print("\nDataFrame with missing values:")
print(df_messy)

# Check for missing values
print("\nMissing values count:")
print(df_messy.isnull().sum())

# Drop rows with missing values
print("\nAfter dropping rows with missing values:")
print(df_messy.dropna())

# Fill missing values
print("\nAfter filling missing values:")
print(df_messy.fillna({'name': 'Unknown', 'age': df_messy['age'].mean(), 'city': 'Unknown'}))

# 6. Basic Calculations
print("\n6. BASIC CALCULATIONS")
print("-" * 50)

# Create numeric DataFrame
df_nums = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

print("\nNumeric DataFrame:")
print(df_nums)

print("\nColumn sums:")
print(df_nums.sum())

print("\nColumn means:")
print(df_nums.mean())

print("\nColumn standard deviations:")
print(df_nums.std())

# 7. Basic Sorting
print("\n7. BASIC SORTING")
print("-" * 50)

print("\nSort by age (ascending):")
print(df1.sort_values('age'))

print("\nSort by age (descending):")
print(df1.sort_values('age', ascending=False))

print("\nSort by multiple columns:")
print(df1.sort_values(['city', 'age']))