import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Customer Sales Project/project/dataset/Customer-Sales-Dataset.csv")
print("Dataset first 10 rows:",data.head(10))
print("Dataset last 5 rows:",data.tail(5))
print("Numeric values:",data.describe())
print("Dataset Shape:", data.shape)
print("Columns Names:", data.columns)
print("Data Type:", data.dtypes)
print("showing Missing Values in each column:",data.isnull().sum())
print("Showing Duplicate Record:", data.duplicated().sum())
print("\nUnique Values:")
print("Region:",data["Region"].nunique())
print("Category:",data["Category"].nunique())
print("Product:",data["Product"].nunique())
print("PaymentMethod:",data["PaymentMethod"].nunique())
#print("OrderStatus:",data["OrderStatus"].nunique())

#now checking the acutal categorical values 


print("\nRegion Transactions:")
print(data["Region"].value_counts(dropna=False))

print("\nCategory Transactions:")
print(data["Category"].value_counts())

before_cleaning = data.shape

print("Shape Before Cleaning:", before_cleaning)

data["Region"] = data["Region"].fillna("Unknown")
print("Missing Region",data["Region"].isnull().sum())

data["UnitPrice"] = data["UnitPrice"].fillna(data["UnitPrice"].median())
print("Missing UnitPrice:", data["UnitPrice"].isnull().sum())

data["DiscountPercent"] = data["DiscountPercent"].fillna(data["DiscountPercent"].median())

print("Missing DiscountPercent:", data["DiscountPercent"].isnull().sum())
print("\nMissing Values After Handling:")
print(data.isnull().sum())

data = data.drop_duplicates()
print("Duplicates Rows after cleaning:", data.duplicated().sum())

data["OrderDate"] = pd.to_datetime(data["OrderDate"])
print("OrderDate data type:", data["OrderDate"].dtype)

print("\nNumeric Data Types:")
print(data[[
    "Quantity",
    "UnitPrice",
    "DiscountPercent",
    "Sales",
    "Cost",
    "Profit"
]].dtypes)

print("\nOrder Status:")
print(data["OrderStatus"].value_counts())

total_sales = data["Sales"].sum()

print("Total Sales:", total_sales)

total_profit = data["Profit"].sum()

print("Total Profit:", total_profit)

average_sales = data["Sales"].mean()

print("Average Sales:", average_sales)

average_profit = data["Profit"].mean()

print("Average Profit:", average_profit)
highest_sales = data.loc[data["Sales"].idxmax()]

print("\nHighest Sales Transaction:", highest_sales)

lowest_sales = data.loc[data["Sales"].idxmin()]
print("\nLowest Sales Transaction:")
print(lowest_sales)

print("Highest Sales:", data["Sales"].max())
print("Lowest Sales:", data["Sales"].min())

total_qty = data["Quantity"].sum()

print("Total Quantity sold:", total_qty)

sales_by_Region = data.groupby("Region")["Sales"].sum()

print("Sales by Region:")
print(sales_by_Region)
sales_by_Category = data.groupby("Category")["Sales"].sum()

print("Sales by Category:")
print(sales_by_Category)

profit_by_category = data.groupby("Category")["Profit"].sum()

print("Profit by Category:")
print(profit_by_category)

sales_by_product = data.groupby("Product")["Sales"].sum()
top_5_products = sales_by_product.sort_values(ascending=False).head(5)
print("Top 5 Products by Sales:")
print(top_5_products)

#--------------
# 1. Category ke hisab se total Profit
profit_by_category = data.groupby("Category")["Profit"].sum()
profit_by_region = data.groupby("Region")["Profit"].sum()
most_profitable_category = profit_by_category.idxmax()
most_profitable_region = profit_by_region.idxmax()
print("Profit by Category:")
print(profit_by_category.sort_values(ascending=False))
print("\nProfit by Region:")
print(profit_by_region.sort_values(ascending=False))
print(f"Most Profitable Category: {most_profitable_category} = {profit_by_category.max():,.2f}")
print(f"Most Profitable Region: {most_profitable_region} = {profit_by_region.max():,.2f}")

#---------------
# 1. Product ke hisab se total Sales aur Profit sum karo
product_summary = data.groupby("Product").agg(Total_Sales = ("Sales", "sum"),Total_Profit = ("Profit", "sum"))
top_sales_product = product_summary["Total_Sales"].idxmax()
highest_sales_value = product_summary["Total_Sales"].max()
top_profit_product = product_summary["Total_Profit"].idxmax()
highest_profit_value = product_summary["Total_Profit"].max()

print("Product Summary:")
print(f"Highest Sales Product: {top_sales_product} = {highest_sales_value:,.2f}")
print(f"Highest Profit Product: {top_profit_product} = {highest_profit_value:,.2f}")

#-----------
sales_by_category = data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sales_by_category.plot(kind='bar', color='pink', edgecolor='black')
plt.title("Sales by Category", fontsize=14, fontweight='bold')
plt.xlabel("Category", fontsize=13)
plt.ylabel("Total Sales", fontsize=13)
plt.xticks(rotation=50, ha='right')
plt.tight_layout()
#plt.savefig("sales_by_category.png")
plt.show()
plt.close()

#--------------
sales_by_region = data[data["Region"] != "Unknown"].groupby("Region")["Sales"].sum().sort_values(ascending=False) / 10000000

plt.figure(figsize=(10,6))
sales_by_region.plot(kind='bar', color='pink', edgecolor='black')

plt.title("Sales by Region", fontsize=14, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
plt.close()

#--------------
# ========== 3. Profit by Category ==========
profit_by_category = data.groupby("Category")["Profit"].sum().sort_values(ascending=False) / 10000000
plt.figure(figsize=(10,6))
profit_by_category.plot(kind='bar', color='yellow', edgecolor='black')

plt.title("Profit by Category", fontsize=14, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Profit", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()
plt.close()

#-----------------
sales_crore = data["Sales"] / 10000000
plt.figure(figsize=(10,6))
plt.hist(sales_crore, bins=30, color='pink', edgecolor='black', alpha=0.7)
plt.title("Sales Distribution Histogram", fontsize=14, fontweight='bold')
plt.xlabel("Sales Amount", fontsize=12)
plt.ylabel("Number of Orders", fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()
plt.close()

#------------
sales_crore = data["Sales"] / 10000000
profit_crore = data["Profit"] / 10000000
plt.figure(figsize=(10,6))
plt.scatter(sales_crore, profit_crore, alpha=0.4, color='pink', edgecolor='black', s=40)
plt.title("Sales vs Profit", fontsize=14, fontweight='bold')
plt.xlabel("Sales", fontsize=12)
plt.ylabel("Profit", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.show()
plt.close()
