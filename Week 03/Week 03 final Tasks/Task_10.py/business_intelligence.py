

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. LOAD DATASET


df = pd.read_csv("Task_10.py/SampleSuperstore.csv")


print("\nFirst 5 Rows")
print(df.head())


print("\nDataset Information")
print(df.info())


print("\nDataset Shape")
print(df.shape)



# 2. DATA CLEANING


print("\nMissing Values")
print(df.isnull().sum())


print("\nDuplicate Rows")
print(df.duplicated().sum())



df = df.drop_duplicates()



# Convert Postal Code

df["Postal Code"] = df["Postal Code"].fillna(0)



# 3. FEATURE ENGINEERING


# Profit Margin

df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
) * 100



# Sales Per Quantity

df["Sales Per Quantity"] = (
    df["Sales"] / df["Quantity"]
)



# Discount Amount

df["Discount Amount"] = (
    df["Sales"] * df["Discount"]
)



# Performance Column


def performance(value):

    if value > 100:
        return "High Profit"

    elif value >= 0:
        return "Low Profit"

    else:
        return "Loss"



df["Performance"] = df["Profit"].apply(performance)



# Loss Order

df["Loss Order"] = df["Profit"] < 0



print("\nFeature Engineering Completed")



# 4. KPI CALCULATION


total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = len(df)

average_sales = df["Sales"].mean()

average_discount = df["Discount"].mean()*100



best_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)



best_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)



best_product = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .idxmax()
)



print("\n========== KPI REPORT ==========")

print("Total Sales:", total_sales)

print("Total Profit:", total_profit)

print("Total Orders:", total_orders)

print("Average Sales:", average_sales)

print("Average Discount:",average_discount,"%")

print("Best Category:",best_category)

print("Best Region:",best_region)

print("Best Product:",best_product)



# 5. EXPORT CLEAN DATASET


df.to_csv(
    "clean_superstore.csv",
    index=False
)


print("\nClean Dataset Exported")



# 6. VISUALIZATION


# Chart 1
# Category Sales Bar Chart


category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
)


plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title(
    "Sales by Category"
)

plt.xlabel(
    "Category"
)

plt.ylabel(
    "Sales"
)

plt.tight_layout()

plt.savefig(
    "category_sales.png"
)

plt.close()



# Chart 2
# Region Sales Pie Chart


region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)



plt.figure(figsize=(7,7))

region_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)


plt.title(
    "Region Sales Distribution"
)

plt.ylabel("")

plt.savefig(
    "region_sales.png"
)

plt.close()



# Chart 3
# Sales vs Profit Scatter


plt.figure(figsize=(8,5))


plt.scatter(
    df["Sales"],
    df["Profit"]
)


plt.title(
    "Sales vs Profit"
)

plt.xlabel(
    "Sales"
)

plt.ylabel(
    "Profit"
)


plt.savefig(
    "sales_profit_scatter.png"
)


plt.close()



# Chart 4
# Profit Histogram


plt.figure(figsize=(8,5))


plt.hist(
    df["Profit"],
    bins=30
)


plt.title(
    "Profit Distribution"
)


plt.xlabel(
    "Profit"
)


plt.ylabel(
    "Frequency"
)


plt.savefig(
    "profit_histogram.png"
)


plt.close()



# Chart 5
# Discount Boxplot


plt.figure(figsize=(8,5))


plt.boxplot(
    df["Discount"]
)


plt.title(
    "Discount Analysis"
)


plt.savefig(
    "discount_boxplot.png"
)


plt.close()



# Chart 6
# Sub Category Sales


sub_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values()
)


plt.figure(figsize=(10,6))


sub_sales.plot(
    kind="barh"
)


plt.title(
    "Sub Category Sales"
)


plt.savefig(
    "subcategory_sales.png"
)


plt.close()



# Chart 7
# Correlation Heatmap


plt.figure(figsize=(8,5))


sns.heatmap(
    df[
        [
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
        ]
    ].corr(),
    annot=True
)


plt.title(
    "Correlation Heatmap"
)


plt.savefig(
    "correlation_heatmap.png"
)


plt.close()



# Chart 8
# Performance Count


plt.figure(figsize=(7,5))


df["Performance"].value_counts().plot(
    kind="bar"
)


plt.title(
    "Order Performance"
)


plt.savefig(
    "performance_chart.png"
)


plt.close()



# 7. FINAL REPORT TEXT


report = f"""

BUSINESS INTELLIGENCE REPORT
============================


Total Sales:
{total_sales}


Total Profit:
{total_profit}


Total Orders:
{total_orders}


Best Category:
{best_category}


Best Region:
{best_region}


Best Selling Sub Category:
{best_product}



Recommendations:

1. Focus marketing on best performing category.

2. Reduce discounts where profit is negative.

3. Improve sales strategy in weak regions.

4. Promote high profit products.


"""


with open(
    "final_report.txt",
    "w"
) as file:

    file.write(report)



print("\nFINAL REPORT CREATED")

print("\nPROJECT COMPLETED SUCCESSFULLY")