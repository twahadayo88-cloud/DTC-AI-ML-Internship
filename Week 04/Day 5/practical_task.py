import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

df = pd.read_csv("Week 04/Day 5/student_classdata.csv")

print(df.head())
print(df.shape)
print(df.describe())
print(df.info())
print(df.isnull().sum())

x=df[["Hours","Attendance","Assignments"]]
y = df[["Marks"]]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_train,y_train)

y_prediction = model.predict(x_test)

print("Predicted values;")
print(y_prediction)

#now comparing both actual and predicted values 
print("\nActual values")
print(y_test)

print("\n Predicted vlues")
print(y_prediction)


mae = mean_absolute_error(y_test, y_prediction)
print("MAE:", mae)

mse = mean_squared_error(y_test,y_prediction)
print("MSE:",mse)

rmse = np.sqrt(mse)
print("RMSE:",rmse)

r2 = r2_score(y_test,y_prediction)
print("R2:", r2)