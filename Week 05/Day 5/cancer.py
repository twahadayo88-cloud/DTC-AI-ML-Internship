import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


from sklearn.model_selection import train_test_split


data = pd.read_csv("Week 05/Day 5/cancer_imbalance.csv")

print(data.head())
print(data.info())
print(data.isnull().sum())
print(data.describe())
print(data.shape)
print(data.columns)

print("\nCancer ")
print(data["Cancer"].value_counts())

x = data.drop("Cancer", axis=1)
y = data["Cancer"]


model = RandomForestClassifier(
    random_state=42
)

scores = cross_val_score(
    model,
    x,
    y,
    cv=5,
    scoring="accuracy"
)

print("Cross Validation Score:")
print(scores)

print("\nMean Cross Validation Accuracy:")
print(scores.mean())

model.fit(x, y)
predictions = model.predict(x)

print("\nPredictions:")
print(predictions)


print("\nAccuracy:")
print(accuracy_score(y,predictions))

print("\nPrecision:")
print(precision_score(y, predictions, zero_division=0))

print("\nRecall:")
print(recall_score(y, predictions, zero_division=0))

print("\nF1 Score:")
print(f1_score(y, predictions, zero_division=0))

cm = confusion_matrix(y, predictions)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    y,
    predictions,
    zero_division=0
))

print("\nActual Cancer Cases:")
print(y.sum())

print("\nPredicted Cancer Cases:")
print(predictions.sum())


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size = 0.01,
    random_state=42,
)

model.fit(
    x_train,
    y_train 
)

predictions = model.predict(x_test)
test_accuracy = accuracy_score(y_test, predictions)

print("\nTest Accuracy:")
print(test_accuracy)

test_accuracy = accuracy_score(y_test, predictions)

print("\nTest Accuracy:")
print(test_accuracy)

new_patient = pd.DataFrame([{
    "Age": 52,
    "Tumor_Size_mm": 34.7,
    "Cell_Density": 0.81,
    "Irregularity": 0.72,
    "Marker_Level": 0.79
}])

new_prediction = model.predict(new_patient)

print("\nNew Patient Prediction:")
print(new_prediction)


new_prediction = model.predict(new_patient)

print("\nNew Patient Prediction:")
print(new_prediction)