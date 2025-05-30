import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = {
    'date': pd.date_range('2024-01-01', periods=10),
    'sales': np.random.randint(100, 1000, 10),
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South', 'North', 'South']
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. Basic Data Exploration
print("Basic Data Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())

# 2. Data Grouping and Aggregation
print("\nAverage sales by category:")
print(df.groupby('category')['sales'].mean())

# 3. Pivot Tables
pivot_table = pd.pivot_table(df, 
                           values='sales',
                           index='category',
                           columns='region',
                           aggfunc='mean')
print("\nPivot table of sales by category and region:")
print(pivot_table)

# 4. Data Filtering
high_sales = df[df['sales'] > 500]
print("\nRows with sales > 500:")
print(high_sales)

# 5. Adding Calculated Columns
df['sales_normalized'] = (df['sales'] - df['sales'].mean()) / df['sales'].std()
print("\nDataFrame with normalized sales:")
print(df.head())

# 6. Time Series Operations
daily_sales = df.set_index('date')['sales']
rolling_avg = daily_sales.rolling(window=3).mean()
print("\nRolling average of sales (3-day window):")
print(rolling_avg)

# 7. Data Reshaping
long_format = df.melt(id_vars=['date', 'category'],
                     value_vars=['sales'],
                     var_name='metric',
                     value_name='value')
print("\nData in long format:")
print(long_format.head())

# Example visualizations
def plot_examples(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Line plot of sales over time
    df.plot(x='date', y='sales', ax=axes[0,0])
    axes[0,0].set_title('Sales Over Time')
    
    # Bar plot of average sales by category
    df.groupby('category')['sales'].mean().plot(kind='bar', ax=axes[0,1])
    axes[0,1].set_title('Average Sales by Category')
    
    # Box plot of sales by region
    df.boxplot(column='sales', by='region', ax=axes[1,0])
    axes[1,0].set_title('Sales Distribution by Region')
    
    # Scatter plot of normalized vs raw sales
    df.plot.scatter(x='sales', y='sales_normalized', ax=axes[1,1])
    axes[1,1].set_title('Normalized vs Raw Sales')
    
    plt.tight_layout()
    return fig

# Create visualization
fig = plot_examples(df)
plt.show()