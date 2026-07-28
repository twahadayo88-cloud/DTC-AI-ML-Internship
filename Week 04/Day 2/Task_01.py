""""import pandas as pd

#load dataset 
df = pd.read_csv("Week 04/Day 2/Students.csv")

#For printing data set
print(df)

#data set information
print(df.info())

#data shape
print(df.shape)

#column names
print(df.columns)

#checking missing values
print(df.isnull().sum())

#total missing values
print(df.isnull().sum().sum())

#checking data type
print(df.dtypes)"""


#______________________________________________________________
# Using dropna (droping rows which are missing)


"""import pandas as pd

df = pd.read_csv("Week 04/Day 2/Students.csv")
print(df)

print("Orignal Shape")
print(df.shape)

df_drop = df.dropna()

print("\nNew Shape")
print(df_drop.shape)

print("\nData set after dropna()")
print(df_drop)"""

#___________________________________________________
# Using fillna (filling rows which are missing)

"""import pandas as pd

df = pd.read_csv("Week 04/Day 2/Students.csv")
print(df)

print("Orignal shape")
print(df.shape)

print(df["Age"].mean())
print(df["Marks"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())



#print(df["City"].mode())
print(df["City"].mode())

#df["City"] = df["City"].fillna(df["City"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])

print(df)"""


#____________________________________________________________________________________________
# Encoding
#Label encodeing

""""import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Week 04/Day 2/Students.csv")

print("Orignal shape")
print(df.shape)

print(df["Age"].mean())
print(df["Marks"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())



#print(df["City"].mode())
print(df["City"].mode())

#df["City"] = df["City"].fillna(df["City"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Remove name
df = df.drop("Name",axis=1)

#Create encoder
encoder = LabelEncoder()

#Encode gender
df["Gender"] = encoder.fit_transform(df["Gender"])

print(df)

print("\nMapping")
print(encoder.classes_)"""

#----------------------------------------------------------------------------
# Encoding
# One Hot Encoding

"""import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Week 04/Day 2/Students.csv")

print("Orignal shape")
print(df.shape)

print(df["Age"].mean())
print(df["Marks"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())



#print(df["City"].mode())
print(df["City"].mode())

#df["City"] = df["City"].fillna(df["City"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Remove name
df = df.drop("Name",axis=1)

#Create encoder
encoder = LabelEncoder()

#Encode gender
df["Gender"] = encoder.fit_transform(df["Gender"])
df = pd.get_dummies(df,columns=["City"])
print("\nAfter one hot encoding")

#print(df)
pd.set_option("display.max_columns",None)
print(df)
print(df.columns)

print("\nMapping")
print(encoder.classes_)"""

#------------------------------------------------------------------------
# Scaling
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Week 04/Day 2/Students.csv")

print("Orignal shape")
print(df.shape)

print(df["Age"].mean())
print(df["Marks"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())



#print(df["City"].mode())
print(df["City"].mode())

#df["City"] = df["City"].fillna(df["City"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Remove name
df = df.drop("Name",axis=1)

#Create encoder
encoder = LabelEncoder()

#Encode gender
df["Gender"] = encoder.fit_transform(df["Gender"])
df = pd.get_dummies(df,columns=["City"])
print("\nAfter one hot encoding")

#Create StandardScaler Objects
scaler=StandardScaler()

#scale age and marks
df[["Age","Marks"]] = scaler.fit_transform(df[["Age","Marks"]])

print("\nAfter Standard Scaling")
print(df)

#print(df)
pd.set_option("display.max_columns",None)
print(df)
print(df.columns)

print("\nMapping")
print(encoder.classes_)