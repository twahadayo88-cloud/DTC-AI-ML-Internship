import pandas as pd
data=pd.read_csv("Task_3.py/student.csv")
#print(data) #printing for whole data
#print(data.head()) #for getting first 5 rows
#print(data.tail())#for getting last 5 rows
#print(data.columns) #For column Names
#print(data.dtypes) #for data type
#print(data.shape[0]) # for number of rows
#print(data.shape[1]) #for number of columns
#print(data["Marks"].describe()) # used for all calculation in one time
#print(data.min())  #use to calculate minimum value
#print(data.max())  #use to calculate the maximum value
#print(data["Marks"].mean()) #use for calculating mean
print(data["Marks"].std()) #use to calculate the standard deviation