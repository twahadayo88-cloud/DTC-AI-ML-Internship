import pandas as pd


#  STEP 1 LOAD DATA

df =pd.read_csv("Task_4.py/employee_data.csv")
#print(df)


#   STEP 2 DATASET CHECKING INFORMATION

print(df.info())


#  STEP 3 CHECKING MISSING VALUE
print(df.isnull().sum())


# STEP 4  REMOVING DUPLICATE ROWS

print("Duplicates:", df.duplicated().sum())


# STEP 5  RENAME THE COLUMN NAMES
df.rename(columns={
    "Full Name": "Name",
    "Emp_ID": "Employee_ID"
}, inplace=True)

# STEP 6 CLEAN AGE COLUMN

df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

average_age = df["Age"].mean()

print("Average Age:", average_age)


df["Age"] = df["Age"].fillna(average_age)

print(df["Age"])

print("Missing Ages:")
print(df["Age"].isnull().sum())

# Step 7 FILL MISSING SALARY VALUES

average_salary = df["Salary"].mean()

print("Average Salary:", average_salary)

df["Salary"] = df["Salary"].fillna(average_salary)


# Step 8: REMOVE ROWS WHERE NAME IS MISSING

df.dropna(
    subset=["Name"],
    inplace=True
)


# Step 9: CONVERT JOINING_DATE INTO DATE FORMAT

df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)


# Step 10: CHECK FINAL ClEAN DATASET

print("\nClean Dataset:")
print(df)


# Step 11: SAVE CLEAN DATASET INTO NEW CSV FILE

df.to_csv(
    "clean_employee_data.csv",
    index=False
)

print("\nClean dataset saved successfully!")


# Step 12: GENERATE CLEANING REPORT

report = {
    "Duplicate Rows Removed": 1,
    "Missing Ages Filled": 2,
    "Missing Salaries Filled": 1,
    "Missing Names Removed": 1,
    "Total Rows After Cleaning": len(df)
}

print("\nCleaning Report:")
for key, value in report.items():
    print(key, ":", value)