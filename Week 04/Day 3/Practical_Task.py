import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


df = pd.read_csv("Week 04/Day 3/titanic.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
print(df.describe())

#feature no 1:
#age category

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[1,12,18,35,60,100],
    labels=["Child","Teen","Adult","Middle Age","Senior"]
)

print(df[["Age","Age_Group"]].head(10))

#feature no 2:
#Family size

df["Family_Size"] = df["SibSp"] + df["Parch"] + 1
print(df[["SibSp","Parch","Family_Size"]].head(10))

#feature no 3:
#Traveling Alone:

df["Is_Alone"] = df["Family_Size"].apply(
    lambda x: "Yes" if x == 1 else "No"
)

print(df[["Family_Size","Is_Alone"]].head(10))


#feature no 4:
#Fare Category:

df["Fare_Category"] = pd.cut(
    df["Fare"],
    bins=[0,10,30,100,600],
    labels=["Low","Medium","High","Luxury"]
)

print(df[["Fare","Fare_Category"]].head(10))

#Feature 5 
# Random Forest Feature

le = LabelEncoder()

df["Sex"]= le.fit_transform(df["Sex"])
df["Embarked"] = df["Embarked"].fillna("Unknown")
df["Embarked"] = le.fit_transform(df["Embarked"])
print(df[["Age","Embarked"]])

df["Age"] = df["Age"].fillna(df["Age"].median())

#using random forest method

X = df[[
    "Pclass",
    "Sex",
    "Age",
    "Fare",
    "Family_Size"
]]

Y = df["Survived"]
model = RandomForestClassifier(random_state=42)
model.fit(X,Y)

#feature importance seeing

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", round(score,3))

#Feature Selection

selected_features = df[[
    "Survived",
    "Pclass",
    "Sex",
    "Age",
    "Fare",
    "Family_Size",
    "Age_Group",
    "Fare_Category"
]]

print(selected_features.head())

correlation = df[[
    "Survived",
    "Pclass",
    "Age",
    "Fare",
    "Family_Size"
]].corr()

print(correlation)


features = X.columns
importance = model.feature_importances_

plt.figure(figsize=(8,5))

plt.bar(features, importance)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.show()


correlation["Survived"].drop("Survived").plot(
    kind="bar",
    figsize=(7,5)
)

plt.title("Features Correlation with Survived")
plt.xlabel("Features")
plt.ylabel("Correlation Value")

plt.grid(axis="y")
plt.show()

import matplotlib.pyplot as plt

features = X.columns
importance = model.feature_importances_

plt.figure(figsize=(8,5))

plt.bar(features, importance)

plt.title("Random Forest Feature Importance", fontsize=14)
plt.xlabel("Features", fontsize=12)
plt.ylabel("Importance Score", fontsize=12)

# Value bars ke upar likho
for i, value in enumerate(importance):
    plt.text(i, value + 0.005, f"{value:.2f}", ha="center")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

#-----------------------------------------
df.to_csv(
    "Week 04/Day 3/feature_titanic.csv",
    index=False
)

print("New dataset saved successfully!")