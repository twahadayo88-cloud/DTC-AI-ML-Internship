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
