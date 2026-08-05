import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


data = pd.read_csv("Week 05/Day 3/diabetes.csv")
print(data.head())
print(data.info())
print(data.shape)
print(data.describe())
print(data.columns)
print(data.isnull().sum())
