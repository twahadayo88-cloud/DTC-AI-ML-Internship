import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans



data = pd.read_csv("Week 06/Day 1/customers.csv")
print(data.head(5))
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())

x = data[[
    "Age",
    "Annual_Income_k",
    "Spending_Score"
]]

plt.scatter(
    data["Annual_Income_k"],
    data["Spending_Score"]
)

plt.xlabel("Annual Income (k)")
plt.ylabel("Spending Score")
plt.title("Customer Data")

plt.show()