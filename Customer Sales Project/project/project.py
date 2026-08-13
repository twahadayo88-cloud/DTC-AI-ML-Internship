import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

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
#plt.savefig("profit_by_category.png")
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
#plt.savefig("sales_vs_profit.png")
plt.show()
plt.close()
#-----------------------------------------------------------------------------------
#part E

correlation_data = data[[
    "Quantity",
    "UnitPrice",
    "DiscountPercent",
    "Sales",
    "Cost",
    "Profit"
]]

print("\nCorrelation Matrix:")
print(correlation_data.corr())
#------------------------------
corr_matrix = correlation_data.corr()
corr_pairs = corr_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs < 1]
strongest_positive_pair = corr_pairs.idxmax()
strongest_positive_value = corr_pairs.max()

print("\nStrongest Positive Relationship:")
print(strongest_positive_pair)
print("Correlation:", strongest_positive_value)

#-----------------------------
print("\nCorrelation with Sales:")
print(correlation_data.corr()["Sales"].sort_values(ascending=False))

#------------------------
discount_profit_corr = correlation_data["DiscountPercent"].corr(
    correlation_data["Profit"]
)
print("\nDiscountPercent vs Profit Correlation:")
print(discount_profit_corr)
#----------------------------------
print("\nComplete Correlation Matrix:")
print(corr_matrix)
#-------------------

# 1. Profit Margin
data["ProfitMargin"] = (data["Profit"] / data["Sales"]) * 100
print("\nProfit Margin:")
print(data[["Sales", "Profit", "ProfitMargin"]].head())

#--------------------
# 2. Discount Amount
data["DiscountAmount"] = (data["Sales"] * data["DiscountPercent"]/ (100 - data["DiscountPercent"]))
print("\nDiscount Amount:")
print(data[["Sales", "DiscountPercent", "DiscountAmount"]].head())

#--------------------------------
# 3. Month
data["Month"] = data["OrderDate"].dt.month
print("\nMonth:")
print(data[["OrderDate", "Month"]].head())
#-------------------------
# 4. Day of Week
data["DayOfWeek"] = data["OrderDate"].dt.day_name()
print("\nDay of Week:")
print(data[["OrderDate", "DayOfWeek"]].head())
#--------------------------------------
# 5. Sales per Item
data["SalesPerItem"] = data["Sales"] / data["Quantity"]
print("\nSales per Item:")
print(data[["Sales", "Quantity", "SalesPerItem"]].head())
#------------------------------
# 6. Cost per Item
data["CostPerItem"] = data["Cost"] / data["Quantity"]
print("\nCost per Item:")
print(data[["Cost", "Quantity", "CostPerItem"]].head())
#-----------------------------------


# part G
sales_median = data["Sales"].median()
print("\nMedian Sales:", sales_median)
data["high_value_purchase"] = (data["Sales"] >= sales_median).astype(int)
print("\nHigh Value Purchase:")
print(data[["Sales", "high_value_purchase"]].head(10))
class_counts = data["high_value_purchase"].value_counts().sort_index()
print("\nClass Counts:")
print(class_counts)
class_percentages = (
    data["high_value_purchase"]
    .value_counts(normalize=True)
    .sort_index() * 100
)
print("\nClass Percentages:")
print(class_percentages)

# Part H - Prepareing data for Machine Learning

predictor_features = [
    "Quantity",
    "UnitPrice",
    "DiscountPercent",
    "Cost",
    "Profit",
    "Region",
    "Category",
    "PaymentMethod",
    "OrderStatus"
]
target = "high_value_purchase"
X = data[predictor_features]
y = data[target]
print("\nPredictor Features:")
print(X.columns)
print("\nTarget:")
print(y.name)
#----------------------
X = pd.get_dummies(
    X,
    columns=[
        "Region",
        "Category",
        "PaymentMethod",
        "OrderStatus"
    ],
    drop_first=True
)
print("\nEncoded Features:")
print(X.head())
print("\nX Shape:", X.shape)
print("y Shape:", y.shape)
print("\nNumber of Model Features:", X.shape[1])

#train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data Shape:")
print(X_train.shape)
print("\nTesting Data Shape:")
print(X_test.shape)
print("\nTraining Labels Shape:")
print(y_train.shape)
print("\nTesting Labels Shape:")
print(y_test.shape)

#---------------
#part I
# Logistic Regression
logistic_model = LogisticRegression(max_iter=1100, random_state=42)
logistic_model.fit(X_train, y_train)
print("\nLogistic Regression model trained successfully.")
logistic_predictions = logistic_model.predict(X_test)
print("\nLogistic Regression Predictions:")
print(logistic_predictions[:11])

# Decision Tree

decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)
print("Decision Tree model trained successfully.")
decision_tree_predictions = decision_tree_model.predict(X_test)
print("\nDecision Tree Predictions:")
print(decision_tree_predictions[:11])

#Accuracy Scores
from sklearn.metrics import accuracy_score
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
decision_tree_accuracy = accuracy_score(y_test, decision_tree_predictions)
print("\nLogistic Regression Accuracy:", logistic_accuracy)
print("Decision Tree Accuracy:", decision_tree_accuracy)

#feature importance for decision tree
feature_importance = decision_tree_model.feature_importances_
print("\nFeature Importance (Decision Tree):")
for feature, importance in zip(X.columns, feature_importance):
    print(f"{feature}: {importance:.4f}")


#confusion matrix for decision tree
from sklearn.metrics import confusion_matrix
decision_tree_cm = confusion_matrix(y_test, decision_tree_predictions)
print("\nConfusion Matrix (Decision Tree):")
print(decision_tree_cm)

#confusion matrix for logistic regression
logistic_cm = confusion_matrix(y_test, logistic_predictions)
print("\nConfusion Matrix (Logistic Regression):")
print(logistic_cm)
logistic_coefficients = pd.Series(
    logistic_model.coef_[0],
    index=X_train.columns
).sort_values(ascending=False)
print("\nLogistic Regression Coefficients:")
print(logistic_coefficients)

#--------------------------
#Part J
#Calculate accuracy, Precision, Recall, and F1-Score for Decision Tree

from sklearn.metrics import classification_report
decision_tree_classification_report = classification_report(y_test, decision_tree_predictions)
print("\nClassification Report (Decision Tree):")
print(decision_tree_classification_report)

#Calculate accuracy, Precision, Recall, and F1-Score for Logistic Regression
logistic_classification_report = classification_report(y_test, logistic_predictions)
print("\nClassification Report (Logistic Regression):")
print(logistic_classification_report)
#confusion matrix for decision tree
print("\nConfusion Matrix (Decision Tree):")
print(decision_tree_cm)
#confusion matrix for logistic regression
print("\nConfusion Matrix (Logistic Regression):")
print(logistic_cm)

#part K
#cross validation for decision tree
cv_scores = cross_val_score(
    decision_tree_model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)
print("\n5-Fold Cross Validation Scores:")
print(cv_scores)
average_cv_score = cv_scores.mean()
print("\nAverage Validation Score:")
print(average_cv_score)
decision_tree_test_predictions = decision_tree_model.predict(X_test)
test_accuracy = accuracy_score(
    y_test,
    decision_tree_test_predictions
)
print("\nTest Accuracy:")
print(test_accuracy)

#part L
feature_importance = pd.Series(
    decision_tree_model.feature_importances_,
    index=X_train.columns
)
print("\nFeature Importance:")
print(feature_importance.sort_values(ascending=False))

#top 5 features
top_5_features = (
    feature_importance
    .sort_values(ascending=False)
    .head(5)
)
print("\nTop 5 Most Important Features:")
print(top_5_features)

#creating bar chart for top 5 features
plt.figure(figsize=(10,6))
top_5_features.plot(kind="bar")
plt.title("Top 5 Most Important Features (Decision Tree)")
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_5_features_decision_tree.png")
plt.show()
