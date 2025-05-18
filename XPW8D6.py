# 📘 Final Exercise Set – Data Visualization with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 🌟 Exercise 1: Understanding Data Visualization
# Why is data visualization important?
# It helps translate complex data into visual formats like charts and graphs, making it easier to identify trends, patterns, and outliers.
# What is the purpose of a line graph?
# Line graphs are used to visualize changes over time and highlight trends in continuous data.

# 🌟 Exercise 2: Creating a Line Plot for Temperature Variation
# Temperature values over a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.figure(figsize=(6, 4))
plt.plot(days, temperatures, marker='o', linestyle='-', color='tomato')
plt.title("Temperature Variation Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🌟 Exercise 3: Visualizing Monthly Sales with a Bar Chart
# Sales data for each month
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(7, 4))
plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales Amount ($)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 🌟 Exercise 4: Data Visualization Using sales_data.csv
# Load the dataset
sales_df = pd.read_csv("your_path_here/sales_data.csv")  # Replace with correct path
sales_df.columns = sales_df.columns.str.strip().str.lower().str.replace(' ', '_')

# Total quantity of products sold
total_quantity = sales_df['quantity'].sum()
print("Total Quantity Sold:", total_quantity)

# Category with highest revenue
sales_df['revenue'] = sales_df['quantity'] * sales_df['price']
revenue_by_category = sales_df.groupby('category')['revenue'].sum()
top_category = revenue_by_category.idxmax()
top_revenue = revenue_by_category.max()
print(f"Top Category by Revenue: {top_category} (${top_revenue:,.2f})")

# Average revenue per sale
average_revenue = sales_df['revenue'].mean()
print(f"Average Revenue Per Sale: ${average_revenue:.2f}")

# Revenue by quarter
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
sales_df['quarter'] = sales_df['order_date'].dt.to_period('Q')
quarterly_revenue = sales_df.groupby('quarter')['revenue'].sum()

# Plotting revenue per quarter
plt.figure(figsize=(7, 4))
quarterly_revenue.plot(kind='bar', color='mediumseagreen')
plt.title("Total Revenue by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🌟 Exercise 5: Data Visualization Using Matplotlib (Line, Bar, Pie)

# Line Plot: y = x^2
x = np.arange(-10, 11)
y = x**2

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='purple')
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Sales of products A–D
products = ['A', 'B', 'C', 'D']
sales_values = [15, 30, 45, 20]

plt.figure(figsize=(6, 4))
plt.bar(products, sales_values, color='orange')
plt.title("Weekly Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

# Pie Chart: Favorite fruits distribution
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [40, 30, 20, 10]
colors = ['red', 'yellow', 'pink', 'brown']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Favorite Fruits Distribution")
plt.legend(fruits, title="Fruits")
plt.tight_layout()
plt.show()