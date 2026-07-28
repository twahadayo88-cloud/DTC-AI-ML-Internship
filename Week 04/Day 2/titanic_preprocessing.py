import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler



df= pd.read_csv("Week 04/Day 2/titanic.csv")

#print(df.head())
#print(df.info())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.isnull().sum())
#print(df.describe())

#remove columns which are unnecessary
df = df.drop(["PassengerId", "Name","Ticket", "Cabin"],axis=1)
print(df.head())
print(df.shape)
print(df.isnull().sum())

print(df["Age"].mean())
print(df["Embarked"].mode()[0])

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.isnull().sum())

print(df.dtypes)

encoder = LabelEncoder()
df["Sex"] = encoder.fit_transform(df["Sex"])
df = pd.get_dummies(df,columns=["Embarked"], dtype=int)
print(df.head())
print(df.shape)
print(encoder.classes_)

scaler = StandardScaler()
df_standard = df.copy()

df_standard[["Age","Fare"]] = scaler.fit_transform(
    df_standard[["Age","Fare"]]
)

print("\nAfter standard scaling")
print(df_standard.head(18))
print(df_standard[["Age","Fare"]].describe())

minmax = MinMaxScaler()
df_minmax = df.copy()

df_minmax[["Age","Fare"]] = minmax.fit_transform(
    df_minmax[["Age","Fare"]]
)

print("\nAfter MinMax Scaling")
print(df_minmax.head())

df_standard.to_csv(
    "Week 04/Day 2/titanic_standard_scaled.csv",
    index=False
)

df_minmax.to_csv(
    "Week 04/Day 2/titanic_minmax_scaled.csv",
    index=False
)