import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

#load dataset
df= pd.read_csv("Week 04/Day 5/std_score.csv")
print(df)

#now selecting the feature and target

x = df[["Hours"]]
y = df[["Marks"]]

#now train test split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


#now creating the linear regression model

model = LinearRegression()

model.fit(x_train, y_train)

y_prediction = model.predict(x_test)

print("Predicted values;")
print(y_prediction)

#now comparing both actual and predicted values 
print("\nActual values")
print(y_test)

print("\n Predicted vlues")
print(y_prediction)


"""#calculating MAE (Mean Absolute error)
mae = mean_absolute_error(y_test, y_prediction)
print("MAE:",mae)"""

#calculating the mean squared error

mse = mean_squared_error(y_test, y_prediction)
print("MSE:",mse)

#calculating the root mean squared error
rmse = np.sqrt(mse)
print("RMSE:",rmse)

#calculating the R2 score

r2 = r2_score(y_test,y_prediction)
print("R2:", r2)