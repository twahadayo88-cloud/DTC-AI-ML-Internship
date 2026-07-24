import pandas as pd


# STEP 1 Load Dataset

df = pd.read_csv("Task_5.py/sales_data.csv")


print(df)
print(df.info())

#STEP 2 CALCULATING TOTAL SALES
total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

#STEP 3 AVERAGE SALES
average_sales = df["Sales"].mean()

print("Average Sales:", average_sales)

#STEP 4 HIGHEST SALES
highest_sale = df["Sales"].max()

print("Highest Sale:", highest_sale)

#STEP 5 LOWEST SALE
lowest_sale = df["Sales"].min()

print("Lowest Sale:", lowest_sale)

#STEP 6 SALES BY CATEGORY
sales_category = df.groupby(
    "Category"
)["Sales"].sum()


print("\nSales By Category:")
print(sales_category)

#STEP 7 TOP 5 PRODUCT
top_products = df.sort_values(
    by="Sales",
    ascending=False
).head(5)


print("\nTop 5 Products:")
print(top_products)