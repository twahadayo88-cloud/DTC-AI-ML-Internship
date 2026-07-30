import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


df = pd.read_csv("Week 04/Day 4/student_score.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

x = df[["Hours"]]
y = df[["Marks"]]

print("\nindependent variable (x):")
print(x.head())

print("\ndependent variable (y):")
print(y.head())

#now we use the train and test split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("\ntraining data shape:")
print(x_train.shape)

print("\ntesting data shape:")
print(x_test.shape)

#train and test model
linear_model = LinearRegression()

linear_model.fit(x_train, y_train)

print("linear regression model trained successfully")

#predicting by using linear regression
linear_prediction = linear_model.predict(x_test)

print("\nactual marks:")
print(y_test.values)

print("\npredicted marks linear regression:")
print(linear_prediction)