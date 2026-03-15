import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first rows
print("First 5 rows of dataset:")
print(df.head())

# Basic dataset information
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values (fill with 0 if any)
df.fillna(0, inplace=True)

# Calculate metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
max_sales = df["Total_Sales"].max()

# Best selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Report
print("\n===== SALES ANALYSIS REPORT =====")
print(f"Total Revenue: ₹{total_sales:,.2f}")
print(f"Average Sale Value: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{max_sales:,.2f}")
print(f"Best Selling Product: {best_product}")

print("\nAnalysis Completed Successfully!")