import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
# Create Images Folder

os.makedirs("images", exist_ok=True)

# Load Dataset

df = pd.read_csv("Week 04/Day 4/house_price_raw.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nDataset Shape")
print(df.shape)

print("\nStatistical Summary")
print(df.describe())

print("\nData Types")
print(df.dtypes)

# Check Missing Values & Duplicates

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# Remove Duplicates

df.drop_duplicates(inplace=True)

print("\nRemaining Duplicates")
print(df.duplicated().sum())

# Fill Missing Values

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

categorical_columns = df.select_dtypes(include=["object"]).columns

df[categorical_columns] = df[categorical_columns].fillna(
    df[categorical_columns].mode().iloc[0]
)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nColumns")
print(df.columns)

# EDA

# Histogram

plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=20)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Houses")
plt.savefig("images/price_distribution.png")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(df["resid_area"], df["price"])
plt.title("Residential Area vs Price")
plt.xlabel("Residential Area")
plt.ylabel("Price")
plt.savefig("images/residential_area_vs_price.png")
plt.show()

# Rooms vs Price

plt.figure(figsize=(8,5))
plt.scatter(df["room_num"], df["price"])
plt.title("Rooms vs Price")
plt.xlabel("Number of Rooms")
plt.ylabel("Price")
plt.savefig("images/rooms_vs_price.png")
plt.show()

# Crime Rate vs Price

plt.figure(figsize=(8,5))
plt.scatter(df["crime_rate"], df["price"])
plt.title("Crime Rate vs Price")
plt.xlabel("Crime Rate")
plt.ylabel("Price")
plt.savefig("images/crime_rate_vs_price.png")
plt.show()

# Correlation Matrix

correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix")
print(correlation)

plt.figure(figsize=(12,8))
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Matrix")
plt.savefig("images/correlation_matrix.png")
plt.show()

# Basic Statistics

print("\nAverage House Price")
print(df["price"].mean())

print("\nHighest House Price")
print(df["price"].max())

print("\nLowest House Price")
print(df["price"].min())
# Encoding

print("\nEncoding Categorical Columns...")

df["airport"] = df["airport"].map({"YES":1, "NO":0})
df["bus_ter"] = df["bus_ter"].map({"YES":1, "NO":0})

df = pd.get_dummies(df, columns=["waterbody"], drop_first=True)

print("\nDataset After Encoding")
print(df.head())

print("\nUpdated Columns")
print(df.columns)

# Feature Selection

X = df.drop("price", axis=1)
y = df["price"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# Linear Regression

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

print("\nLinear Regression Model Trained Successfully")

linear_prediction = linear_model.predict(X_test)

print("\nFirst 10 Linear Predictions")

print(linear_prediction[:10])
# Decision Tree

tree_model = DecisionTreeRegressor(random_state=42)

tree_model.fit(X_train, y_train)

print("\nDecision Tree Model Trained Successfully")

tree_prediction = tree_model.predict(X_test)

print("\nFirst 10 Tree Predictions")

print(tree_prediction[:10])

# Comparison Table

comparison = pd.DataFrame({

    "Actual Price": y_test.values,

    "Linear Prediction": linear_prediction.round(2),

    "Tree Prediction": tree_prediction.round(2)

})

print("\nComparison Table")

print(comparison.head(10))

comparison.to_csv(
    "comparison_results.csv",
    index=False
)

print("\nComparison Results Saved Successfully!")
# Model Evaluation

linear_score = linear_model.score(X_test, y_test)

tree_score = tree_model.score(X_test, y_test)

print("\nLinear Regression Score :", linear_score)

print("Decision Tree Score :", tree_score)

# =====================================================
# Final Result
# =====================================================

print("\n========== FINAL RESULT ==========")

if linear_score > tree_score:
    print("Linear Regression performed better.")

elif tree_score > linear_score:
    print("Decision Tree performed better.")

else:
    print("Both models performed equally.")

print("\nProject Completed Successfully!")