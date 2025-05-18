# 📊 Data Science Job Salary Dataset - Analysis Script

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
# Make sure the CSV file is in the same directory or provide the full path
df = pd.read_csv("/Users/sam/Documents/DI_DATA_2025/week8/Data Science Job Salary dataset/ds_salaries.csv")

# Step 2: Normalize the 'salary' column using Min-Max normalization
scaler = MinMaxScaler()
df['salary_normalized'] = scaler.fit_transform(df[['salary']])

# Step 3: Dimensionality Reduction using PCA
# Select only numeric columns for dimensionality reduction
numeric_cols = df.select_dtypes(include='number').drop(columns=['salary']).columns
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df[numeric_cols])
df['PCA1'] = pca_result[:, 0]
df['PCA2'] = pca_result[:, 1]

# Optional: t-SNE for better visualization (comment/uncomment if needed)
# tsne = TSNE(n_components=2, random_state=42)
# tsne_result = tsne.fit_transform(df[numeric_cols])
# df['TSNE1'] = tsne_result[:, 0]
# df['TSNE2'] = tsne_result[:, 1]

# Step 4: Group by experience level and compute average & median salary
salary_summary = df.groupby('experience_level')['salary'].agg(['mean', 'median']).reset_index()
print("\n📌 Salary summary by experience level:")
print(salary_summary)

# Step 5: Visualize average vs. median salaries by experience level
plt.figure(figsize=(10, 6))
sns.barplot(data=salary_summary, x='experience_level', y='mean', color='skyblue', label='Average Salary')
sns.barplot(data=salary_summary, x='experience_level', y='median', color='orange', label='Median Salary')
plt.title('Average and Median Salary by Experience Level')
plt.ylabel('Salary in USD')
plt.legend()
plt.show()

# Step 6: Optional PCA visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='experience_level', palette='Set2')
plt.title("PCA - Dimensionality Reduction by Experience Level")
plt.show()