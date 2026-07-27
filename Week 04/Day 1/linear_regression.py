import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Week 04/Day 1/STD_score.csv")
print(df)

x =df[["Hours"]]
y=df["Marks"]

x_train, x_test, y_train, y_test = train_test_split(

x,
y,
test_size=0.2,
random_state=42
)
print("Training Data ")
print(x_train)

print("\nTesting Data")
print(x_test)

print("Traing Data")
print(y_train)

print("\nTesting Data")
print(y_test)