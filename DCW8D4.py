# 📘 Daily Challenge - Day 4: Data Analysis on Data Science Job Salaries

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
file_path = "/Users/sam/Documents/DI_DATA_2025/week8/Data Science Job Salary dataset/ds_salaries.csv" 
df = pd.read_csv(file_path)

# Step 3: Clean column names for consistency
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 4: Identify data types
# Quantitative data: salary
# Qualitative data: job_title, job_type, experience_level, location, salary_currency
print("Data types:")
print(df.dtypes)

# Step 5: Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())
df = df.dropna()  # Remove any rows with missing values (if any)

# Step 6: Remove duplicates
print("\nNumber of rows before removing duplicates:", len(df))
df = df.drop_duplicates()
print("Number of rows after removing duplicates:", len(df))

# Step 7: Group-wise analysis by experience_level
grouped = df.groupby('experience_level')['salary'].agg(['mean', 'median']).reset_index()
print("\nMean and median salary by experience level:")
print(grouped)

# Step 8: Bar chart for average salary by experience level
plt.figure(figsize=(8, 5))
plt.bar(grouped['experience_level'], grouped['mean'], color='skyblue')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary (USD)')
plt.title('Average Salary by Experience Level')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()