import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("Week 05/Day 2/project/Iris.csv")
print(data.head(5))
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.columns)

print(data.drop(columns=["Id", "Species"]))

x = data[[
    "SepalLengthCm", 
    "SepalWidthCm", 
    "PetalLengthCm", 
    "PetalWidthCm"
    ]]
y =data["Species"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
knn_predictions = knn.predict(x_test)

print("Actusal Values")
print(y_test)

print()

print("Predicted Values")
print(knn_predictions)


knn_accuracy = accuracy_score(y_test,knn_predictions)

print("KNN Accuracy:",knn_accuracy * 100, "%")

#----------------------------------------------------------

dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)

dt_predictions = dt.predict(x_test)

print("Actual Values")
print(y_test)

print()

print("Decision Tree Predicted values")
print(dt_predictions)

dt_accuracy = accuracy_score(y_test, dt_predictions)
print("Decision Tree Accuracy:", dt_accuracy * 100, "%")

#-----------------------------------------
print("\n------Model Comparison-----------")
print("KNN Accuracy:", knn_accuracy * 100, "%")
print("Decision Tree Accuracy:", dt_accuracy * 100, "%")
