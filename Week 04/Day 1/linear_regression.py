import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv("Week 04/Day 1/STD_score.csv")
print(df)

x =df[["Hours"]]
y=df["Marks"]

x_train, x_test, y_train, y_test = train_test_split(

x,
y,
test_size=0.3,
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

model = LinearRegression()
model.fit(x_train, y_train)
print("\nModel Train Now")

new_student = [[6.5]]
predicted_marks = model.predict(new_student)


print("\nNew student Hours:", new_student[0][0])
print("prediction Marks:", predicted_marks[0])

print("\n Actual Marks")
print(y_test.values)

print("\n Predicted Marks")
print(predicted_marks)

plt.scatter(x,y)
plt.plot(x, model.predict(x))
plt.xlabel("study hours")
plt.ylabel("marks")
plt.title("study hours vs marks")
plt.show()