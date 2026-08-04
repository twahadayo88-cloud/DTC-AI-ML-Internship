import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("Week 05/Day 2/student.csv")
print(data.head())

x = data[["Hours"]]
y = data["Result"]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y, 
    test_size=0.2, 
    random_state=42
)

print(x_train.shape, x_test.shape,
      y_train.shape, y_test.shape
)

#creating KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

#making predictions
knn_predictions = knn.predict(x_test)
print("KNN Predictions:", knn_predictions)

#calculating accuracy
knn_accuracy = accuracy_score(y_test, knn_predictions)
print("KNN Accuracy:", knn_accuracy)

#creating Decision Tree model
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train,y_train)

dt_predictions = dt.predict(x_test)

print("Actual Values:")
print(y_test)

print()

print("Decision Tree Predictions:")
print(dt_predictions)

#calculating the accuraccy

dt_accuracy = accuracy_score(y_test, dt_predictions)
print("Decision Tree Accuracy:", dt_accuracy * 100, "%")

#now comparing both models

print("\n--------Model Comparion----------")
print("KNN Accuracy:", knn_accuracy * 100, "%")
print("Decision Tree Accuracy:", dt_accuracy * 100, "%")
