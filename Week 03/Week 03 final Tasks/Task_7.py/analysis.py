import pandas as pd
import matplotlib.pyplot as plt

# STEP 1 LOAD DATASET


df = pd.read_csv("Task_7.py/sales_dataset.csv")

print(df)

# STEP 2 DATASET INFORMATION

print(df.info())

print(df.shape)

# STEP 3 CHECK MISSING VALUES

print(df.isnull().sum())

# STEP 4 REMOVE DUPLICATES

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# STEP 5 REMOVE MISSING VALUES

df = df.dropna()

# STEP 6: CONVERT DATE

df["Date"] = pd.to_datetime(df["Date"])

# STEP 7 FEATURE ENGINEERING

print("\nCreating New Features...")

# Feature 1
df["Year"] = df["Date"].dt.year

# Feature 2
df["Month"] = df["Date"].dt.month_name()

# Feature 3
df["Day"] = df["Date"].dt.day_name()

# Feature 4
df["Discount"] = df["Sales"] * 0.05

# Feature 5
df["Net_Sales"] = df["Sales"] - df["Discount"]

print(df.head())

# STEP 8 SAVE CLEAN DATASET

df.to_csv("clean_sales_dataset.csv", index=False)

# STEP 9 BASIC ANALYSIS

print("\n BUSINESS ANALYSIS:")

total_sales = df["Sales"].sum()

average_sales = df["Sales"].mean()

highest_sale = df["Sales"].max()

lowest_sale = df["Sales"].min()

print("Total Sales :", total_sales)

print("Average Sales :", average_sales)

print("Highest Sale :", highest_sale)

print("Lowest Sale :", lowest_sale)

# STEP 10 SALES BY CATEGORY

print("\nSales By Category")

category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

# STEP 11 SALES BY CITY


print("\nSales By City")

city_sales = df.groupby("City")["Sales"].sum()

print(city_sales)

# STEP 12 MONTHLY SALES

print("\nMonthly Sales")

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

# STEP 13 TOP 5 PRODUCTS

print("\nTop 5 Products")

top_products = df.sort_values(
    by="Sales",
    ascending=False
).head(5)

print(top_products)

# STEP 14 RELATIONSHIP ANALYSIS

print("\nPrice and Sales Relationship")

relationship = df[["Price", "Sales"]].corr()

print(relationship)

# STEP 15 OUTLIER DETECTION

Q1 = df["Sales"].quantile(0.25)

Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)

upper_limit = Q3 + (1.5 * IQR)

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\nOutliers")

print(outliers)

# STEP 16 SUMMARY REPORT

print("\n FINAL REPORT:")

print("Total Records :", len(df))

print("Duplicate Rows Removed :", duplicates)

print("Total Sales :", total_sales)

print("Average Sales :", round(average_sales, 2))

print("Highest Sale :", highest_sale)

print("Lowest Sale :", lowest_sale)

print("\nAll Task Complete")

# CHART 1 LINE CHART

import matplotlib.pyplot as plt

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.plot(monthly_sales.index,
         monthly_sales.values,
         marker="o")

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("line_chart.png")

plt.show()


# CHART 2 BAR CHART

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.bar(category_sales.index,
        category_sales.values)

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("bar_chart.png")

plt.show()

# CHART 3  SCATTER PLOT

plt.figure(figsize=(8,5))

plt.scatter(df["Price"],
            df["Sales"])

plt.title("Price vs Sales")

plt.xlabel("Price")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("scatter_plot.png")

plt.show()

# CHART 4 : HISTOGRAM
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.hist(df["Sales"],
         bins=6)

plt.title("Sales Distribution")

plt.xlabel("Sales")

plt.ylabel("Frequency")

plt.grid(True)

plt.savefig("histogram.png")

plt.show()

# CHART 5 : PIE CHART

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,6))

plt.pie(category_sales,
        labels=category_sales.index,
        autopct="%1.1f%%")

plt.title("Sales by Category")

plt.savefig("pie_chart.png")

plt.show()

