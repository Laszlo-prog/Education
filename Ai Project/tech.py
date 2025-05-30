import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create sample customer purchase data
np.random.seed(42)

# Generate synthetic data
n_customers = 200
data = {
    'customer_id': range(1, n_customers + 1),
    'purchase_amount': np.random.normal(100, 30, n_customers),
    'frequency': np.random.poisson(5, n_customers),
    'recency_days': np.random.randint(1, 365, n_customers)
}

# Create DataFrame
df = pd.DataFrame(data)

# Basic data exploration with Pandas
print("=== Data Overview ===")
print(df.describe())

# Add a derived feature
df['avg_purchase'] = df['purchase_amount'] / df['frequency']

# Prepare data for clustering
features = ['purchase_amount', 'frequency', 'recency_days']
X = df[features]

# Standardize features using scikit-learn
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Create visualizations
plt.figure(figsize=(15, 5))

# Plot 1: Purchase Amount Distribution
plt.subplot(131)
sns.histplot(data=df, x='purchase_amount', bins=30)
plt.title('Distribution of Purchase Amounts')
plt.xlabel('Purchase Amount ($)')

# Plot 2: Scatter plot with clusters
plt.subplot(132)
sns.scatterplot(data=df, x='purchase_amount', y='frequency',
                hue='cluster', palette='deep')
plt.title('Customer Segments')
plt.xlabel('Purchase Amount ($)')
plt.ylabel('Purchase Frequency')

# Plot 3: Box plot of purchase amounts by cluster
plt.subplot(133)
sns.boxplot(data=df, x='cluster', y='purchase_amount')
plt.title('Purchase Amount by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Purchase Amount ($)')

plt.tight_layout()

# Calculate cluster statistics using pandas
cluster_stats = df.groupby('cluster').agg({
    'purchase_amount': ['mean', 'count'],
    'frequency': 'mean',
    'recency_days': 'mean'
}).round(2)

print("\n=== Cluster Analysis ===")
print(cluster_stats)

# Find top customers using pandas
top_customers = df.nlargest(5, 'purchase_amount')[
    ['customer_id', 'purchase_amount', 'frequency', 'cluster']
]
print("\n=== Top 5 Customers ===")
print(top_customers)