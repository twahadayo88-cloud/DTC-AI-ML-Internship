import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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