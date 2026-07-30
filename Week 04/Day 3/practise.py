import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week 04/Day 3/students_data.csv")

print(df)
print(df.info())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
print(df.dtypes)

#--------------------------------------------------
# Feature Engineering
#creating age groups

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,20,23,100],
    labels=["Young","Adult","Senior"]

)

print(df[["Age","Age_Group"]])

#Creating Pass/Fail 
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x>=50 else"Fail"
)

print(df[["Marks","Result"]])


#grade feature
def grade(mark):
    if pd.isna(mark):
        return"Missing"
    elif mark >= 90:
        return"A"
    elif mark >=80:
        return"B"
    elif mark >=70:
        return"C"
    else:
        return"D"

df["Grade"] = df["Marks"].apply(grade)
print(df[["Marks", "Grade"]])


#Percentage of Marks

df["Percentage"] =(df["Marks"]/100)*100
print(df[["Marks", "Percentage"]])


print(df)

#-------------------------------------------------------
# Feature Selection

#selecting useful features

selected_features = df[[
    "Gender",
    "Age",
    "Marks",
    "Grade",
    "Result"
]]

print(selected_features)

#removing unnecessary colums

new_df = df.drop(columns=["Name","City"])

print(new_df)

# correlation analysis

correlation = df[["Age","Marks","Percentage"]].corr()
print(correlation)


plt.figure(figsize=(6,4))
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")

plt.show()

#save updated dataset
df.to_csv("feature_engineered_students.csv", index=False)

print("Dataset Saved Successfully!")

#verify dataset saved or not
saved_df = pd.read_csv("feature_engineered_students.csv")

print(saved_df.head())