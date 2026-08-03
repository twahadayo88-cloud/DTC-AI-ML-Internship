""""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("Week 05/Day 1/student.csv")
print(data.head(5))

x = data[["Hours"]]
y = data["Pass"]

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42

)

print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

model = LogisticRegression()
#print(model)

model.fit(x_train, y_train)
#print("Model trained successfully.")

predictions = model.predict(x_test)
print("Predictions:", predictions)


print("Predicted Values:", predictions)
print("Actual Values:",)
print(y_test.values)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
print(f"Model Accuracy: {accuracy * 100:.2f}%")"""



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("Week 05/Day 1/student.csv")

print(data.head(5))
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.shape)


x = data[["Hours", "Attendance"]]
y = data["Result"]

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Predictions:", y_pred)

#compare predicted values with actual values
print("Predicted Values:", y_pred)
print("Actual Values:", y_test.values)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#probability of passing the exam based on hours studied and attendance
probability = model.predict_proba(x_test)

print("Prediction Probabilities:")
print(probability)



