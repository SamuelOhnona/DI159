# 📊 World Happiness Report Analysis (2019)
# File structure: Archive_kaggle_ds/2019.csv

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the 2019 dataset
file_path = '/Users/sam/Documents/DI_DATA_2025/week8/Archive_Kaggle_ds/2019.csv'
df = pd.read_csv(file_path)

# Step 2: Inspect the data structure
print("\n🔍 First 5 rows of the dataset:")
print(df.head())

print("\n🧾 Columns in dataset:")
print(df.columns)

# Step 3: Rename columns for consistent access (if needed)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Step 4: Check for missing values
print("\n❓ Missing values per column:")
print(df.isnull().sum())

# Step 5: Drop rows with missing values (or handle as needed)
df = df.dropna()

# --- SOCIAL SUPPORT & HAPPINESS SCATTERPLOT ---

# Step 6: Scatter plot between Social_Support and Happiness_Score
plt.figure(figsize=(10, 6))
plt.scatter(df['Social_support'], df['Score'], alpha=0.7, color='royalblue')
plt.title('Social Support vs Happiness Score (2019)', fontsize=14)
plt.xlabel('Social Support')
plt.ylabel('Happiness Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- GDP & HEALTHY LIFE EXPECTANCY BY REGION ---

# Step 7: If region is not provided in the 2019 data, manually map some
# (You can load a region map file or create a dictionary)
# For this example, we'll just proceed without region grouping.

# Step 8: Sort data for plotting
df_sorted = df.sort_values('GDP_per_capita', ascending=False)

# Step 9: Create subplot comparing GDP and Healthy Life Expectancy
fig, ax1 = plt.subplots(figsize=(14, 6))

# Bar plot for GDP per Capita
ax1.bar(df_sorted['Country_or_region'], df_sorted['GDP_per_capita'], color='skyblue', label='GDP per Capita')
ax1.set_xlabel('Country', fontsize=12)
ax1.set_ylabel('GDP per Capita', color='blue', fontsize=12)
ax1.tick_params(axis='x', rotation=90)
ax1.tick_params(axis='y', labelcolor='blue')

# Line plot for Healthy Life Expectancy
ax2 = ax1.twinx()
ax2.plot(df_sorted['Country_or_region'], df_sorted['Healthy_life_expectancy'], color='green', marker='o', label='Healthy Life Expectancy')
ax2.set_ylabel('Healthy Life Expectancy', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')

plt.title('GDP per Capita and Healthy Life Expectancy by Country (2019)', fontsize=14)
fig.tight_layout()
plt.show()