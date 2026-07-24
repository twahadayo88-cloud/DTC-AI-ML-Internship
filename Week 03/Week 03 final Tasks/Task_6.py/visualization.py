import pandas as pd
import matplotlib.pyplot as plt

#STEP 1 LOAD DATASET

df=pd.read_csv("Task_6.py/sales_data.csv")
print(df)

#STEP 2 LINE CHART
"""plt.figure(figsize=(8,5))

plt.plot(df["Product"], df["Sales"], marker="o")

plt.title("Sales Trend")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("line_chart.png")

plt.show()"""

#STEP 3 BAR CHART

"""plt.figure(figsize=(8,5))

plt.bar(df["Product"], df["Sales"])

plt.title("Sales by Product")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("bar_chart.png")

plt.show()"""

#STEP 4 SCATTER PLOT

"""plt.figure(figsize=(8,5))

plt.scatter(df["Price"], df["Sales"])

plt.title("Price vs Sales")

plt.xlabel("Price")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("scatter_plot.png")

plt.show()"""

#STEP 5 HISTOGRAM

plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=5)

plt.title("Sales Distribution")

plt.xlabel("Sales")

plt.ylabel("Frequency")

plt.grid(True)

plt.savefig("histogram.png")

plt.show()