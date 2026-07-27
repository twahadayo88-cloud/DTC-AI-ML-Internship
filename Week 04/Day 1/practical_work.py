import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Week 04/Day 1/StudentsPerformance.csv")



print(df.head())
print(df.shape)
print(df.info())
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())

x= df[["math score", "reading score"]]
y=df["writing score"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=80,
    random_state=20
)
print ("\nTraining Data")
print(x_train)

print("\nTesting Data")
print(x_test)

print("\nTraining Data")
print(y_train)

print("\nTesting Data")
print(y_test)


model = LinearRegression()

model.fit(x_train, y_train)

y_prediction = model.predict(x_test)

print("\nActual Writing Scores:")
print(y_test)

print("\nPredicted Writing Scores:")
print(y_prediction)

#comparing bot actual value and predicted value 

comparison = pd.DataFrame({
    "Actual Writing Score": y_test.values,
    "Predicted Writing Score": y_prediction
})
 
print(comparison)

#R2 Score Model ke accuracy check karny ky liya use kar rahy hh

r2 = r2_score(y_test, y_prediction)
print("R2 Score",r2)

#MAE Mean Absolute Error

mea = mean_absolute_error(y_test, y_prediction)
print("Mean Absolute Error:", mea)

#MSE Mean Square Error
mse = mean_squared_error(y_test, y_prediction)
print("Mean Squared Error:", mse)



#graph

plt.figure(figsize=(10,6))

plt.scatter(y_test, y_prediction)

plt.xlabel("Actual Writing Score")
plt.ylabel("Predicted Writing Score")
plt.title("Actual vs Predicted Writing Score")

plt.show()