import pandas as pd
import matplotlib.pyplot as plt

#LOAD DATASET
df = pd.read_csv("Task_8.py/SampleSuperstore.csv")
print(df.head())

# SYEP 2 Dataset Information
print("\nDATASET INFO")
print(df.info())


#STEP 3 SHAPE
print(df.shape)

# STEP 4 MISSING VALUES
print(df.isnull().sum())

# STEP 5 DUPLICATE ROWS
print(df.duplicated().sum())
df = df.drop_duplicates()

#STEP 6 STATISTICS
print(df.describe())

#STEP 7 COLUMNS
print(df.columns)

#STEP 8 SAVING CLEAN DATA
df.to_csv(
    "clean_superstore.csv",
    index=False
)

print("Dataset Save Successfully")

#STEP 8 TOTAL SALES
print("\nTOTAL SALES:")

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

#STEP 9 TOTAL PROFT
print("\nTOTAL PROFIT:")

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

#STEP 10 AVERAGE SALES
print("\nAVERAGE SALES:")

average_sales = df["Sales"].mean()

print("Average Sales:", average_sales)

#STEP 11 HIGHEST SALE
print("\nHIGHEST SALE:")

highest_sale = df["Sales"].max()

print("Highest Sale:", highest_sale)

#STEP 12 LOWEST SALES:
print("\nLOWEST SALES:")

lowest_sale = df["Sales"].min()

print("Lowest Sale:", lowest_sale)

#STEP 13 SALES BY CATEGORY
print("\nSALES BY CATEGORY:")

sales_category = df.groupby("Category")["Sales"].sum()

print(sales_category)

#STEP 14 PROFIT BY CATEGORY
print("\nPROFIT BY CATEGORY:")

profit_category = df.groupby("Category")["Profit"].sum()

print(profit_category)

#STEP 15 SALES BY REGION
print("\nSALES BY REGION:")

sales_region = df.groupby("Region")["Sales"].sum()

print(sales_region)

#STEP 16 PROFIT BY REGION
print("\nPROFIT BY REGION:")

profit_region = df.groupby("Region")["Profit"].sum()

print(profit_region)

#STEP 17 TOP 10 CITIES BY SALES
print("\nTOP 10 CITIES BY SALES:")

top_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_cities)

#STEP 18 TOP 10 STATES BY PROFIT
print("\nTOP 10 STATES BY PROFIT:")

top_states = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(10)

print(top_states)

#STEP 19 TOP 10 PRODUCTS (SUB CATEGORY)
print("\nTOP 10 PRODUCTS (SUB CATEGORY:")

top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)

#STEP 20 SEGMENT WISE SALES
print("\nSEGMENT WISE SALES:")

segment_sales = df.groupby("Segment")["Sales"].sum()

print(segment_sales)

#STEP 21 CORRELATION ANALYSIS
print("\nCORRELATION ANALYSIS:")

correlation = df[["Sales","Profit","Quantity","Discount"]].corr()

print(correlation)

#STEP 22 PIVOT TABLE
print("\nPIVOT TABLE:")

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Category",
    columns="Region",
    aggfunc="sum"
)

print(pivot)

# STEP 16 FILTERING

print("\nFILTERING:")

furniture = df[df["Category"] == "Furniture"]

print("\nFurniture Category")
print(furniture.head())

print("Total Furniture Sales:", furniture["Sales"].sum())



west = df[df["Region"] == "West"]

print("\nWest Region")
print(west.head())

print("West Region Sales:", west["Sales"].sum())



high_profit = df[df["Profit"] > 500]

print("\nHigh Profit Orders (Profit > 500)")
print(high_profit)



discount_orders = df[df["Discount"] > 0]

print("\nOrders Having Discount")
print(discount_orders.head())


# STEP 17 OUTLIER DETECTION

print("\n OUTLIER DETECTION ")

Q1 = df["Sales"].quantile(0.25)

Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)

upper_limit = Q3 + (1.5 * IQR)

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print(outliers)

print("\nTotal Outliers:", len(outliers))

# STEP 18  SAVE OUTLIERS

outliers.to_csv(
    "outliers.csv",
    index=False
)

print("\nOutliers save successfully!")


# STEP 19 : FEATURE ENGINEERING

print("\nFEATURE ENGINEERING:")


df["Sales_Per_Quantity"] = df["Sales"] / df["Quantity"]

df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

print(df.head())



df.to_csv(
    "final_superstore.csv",
    index=False
)

print("\nFinal dataset saved successfully!")

# STEP 20 FINAL SUMMARY

print("\nFINAL SUMMARY")

print("Total Records :", len(df))

print("Total Sales :", df["Sales"].sum())

print("Total Profit :", df["Profit"].sum())

print("Average Sales :", round(df["Sales"].mean(), 2))

print("Highest Sale :", df["Sales"].max())

print("Lowest Sale :", df["Sales"].min())

print("Total Outliers :", len(outliers))

print("\nTask 8 EDA Completed Successfully!")


#--------------------------------------------------------------------------
# STEP 21 VISUALIZATIONS


# CHART 1 : LINE CHART
# Monthly Sales Trend

print("\nCreating Line Chart...")

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.plot(
    category_sales.index,
    category_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Sales by Category (Line Chart)")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.grid(True)

plt.savefig("line_chart.png")

plt.show()


# CHART 2 : BAR CHART
# Sales by Region

print("Creating Bar Chart...")

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.grid(True)

plt.savefig("bar_chart.png")

plt.show()


# CHART 3 : PIE CHART
# Sales by Segment

print("Creating Pie Chart...")

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Segment")

plt.savefig("pie_chart.png")

plt.show()


# CHART 4 : SCATTER PLOT
# Sales vs Profit

print("Creating Scatter Plot...")

plt.figure(figsize=(8,5))

plt.scatter(
    df["Sales"],
    df["Profit"]
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.savefig("scatter_plot.png")

plt.show()


# CHART 5 : HISTOGRAM
# Sales Distribution

print("Creating Histogram...")

plt.figure(figsize=(8,5))

plt.hist(
    df["Sales"],
    bins=20
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("histogram.png")

plt.show()


# CHART 6 : BOX PLOT
# Outlier Detection

print("Creating Box Plot...")

plt.figure(figsize=(8,5))

plt.boxplot(df["Sales"])

plt.title("Box Plot of Sales")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("box_plot.png")

plt.show()


# CHART 7 : CORRELATION HEATMAP

print("Creating Correlation Heatmap...")

correlation = df[
    ["Sales", "Profit", "Quantity", "Discount"]
].corr()

plt.figure(figsize=(6,5))

plt.imshow(
    correlation,
    cmap="coolwarm",
    interpolation="nearest"
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.savefig("heatmap.png")

plt.show()


# FINAL MESSAGE

print(" All Charts Created Successfully!")
print(" Task 8 (EDA) Completed Successfully!")
