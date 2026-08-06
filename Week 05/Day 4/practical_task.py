import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Week 05/Day 4/diabetes.csv")
print(data.head())
print(data.info())
print(data.columns)
print(data.isnull().sum())
print(data.describe())
print(data.shape)

x = data.drop("Outcome", axis=1)
y = data["Outcome"]


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42
)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)




model.fit(x_train, y_train)
y_predictions = model.predict(x_test)
print(y_predictions)

cm = confusion_matrix(
    y_test,
    y_predictions
)

print(cm)

#visualize confusion matrix

plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()

#Accuracy

accuracy = accuracy_score(
    y_test,
    y_predictions
)

print("Accuracy:", accuracy)

#precision

precision = precision_score(
    y_test,
    y_predictions
)

print("Precision:", precision)

#recall

recall = recall_score(
    y_test,
    y_predictions
)


print("Recall:", recall)

#F1 Score:

f1 = f1_score(
    y_test,
    y_predictions
)


print("F1 Score:", f1)

#making table for comparison
results = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],

    "Score":[
        accuracy,
        precision,
        recall,
        f1
    ]
})


print(results)

# Feature Importance

importance = model.feature_importances_

feature_importance = pd.DataFrame({

    "Feature": x.columns,

    "Importance": importance

})


print(feature_importance)


#sorting the feature importance

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)


print(feature_importance)

#Making graph
plt.figure(figsize=(8,5))


sns.barplot(
    x="Importance",
    y="Feature",
    data=feature_importance
)


plt.title("Feature Importance in Diabetes Prediction")

plt.savefig("feature_importance.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()