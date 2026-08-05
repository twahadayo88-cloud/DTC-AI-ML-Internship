import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


data = pd.read_csv("Week 05/Day 3/diabetes.csv")
print(data.head())
print(data.info())
print(data.shape)
print(data.describe())
print(data.columns)
print(data.isnull().sum())

x = data.drop("Outcome", axis=1)
y = data["Outcome"]

print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=(0.2),
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(x_train, y_train)
y_prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, y_prediction)
print("Accuracy:", accuracy * 100)

#Feature importance

importance = model.feature_importances_
#print(importance)

feature_importance = pd.DataFrame({
    "Feature": x.columns,
    "Importance": importance
})

print(feature_importance)

# Sorting the important features

feature_importance = feature_importance.sort_values(
    by = "Importance",
    ascending=False
)

print(feature_importance)