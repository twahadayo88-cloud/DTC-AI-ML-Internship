#import pandas as pd
#import os

#current_dir = os.path.dirname(__file__)
#csv_path = os.path.join(current_dir, "datasets", "students.csv")

#df = pd.read_csv(csv_path)
#print(df)

#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe())
#print(df.info)

#-----------------------
# Simple Pandas DataFrame
#import pandas as pd

#data = {
  #"calories": [420, 380, 390, 200, 670, 313, 250],
  #"duration": [50, 40, 45, 60, 70, 56, 69],
  #"days": ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
#}

#load data into a DataFrame object:
#df = pd.DataFrame(data)

#print(df)

#----------------------- 
# Refer to the row index
# ----------------------
#print(df.loc[0])

#print(df.loc[[0,1,2]])
#-------------------------------------------------------



#import pandas as pd

#data = {
  #"calories": [420, 380, 390, 200, 670, 313, 250],
  #"duration": [50, 40, 45, 60, 70, 56, 69],
  #"days": ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
#}

#load data into a DataFrame object:
#df = pd.DataFrame(data, index=["day1",
        #"day2",
        #"day3",
        #"day4",
        #"day5",
        #"day6",
        #"day7"])
#print(df)
#______________________
# locate the name index
#print(df.loc["day2"])

#------------------------------------------------------ 
# Load files into a dataframe
#import pandas as pd
#df = pd.read_json("datasets/students.csv")
#df = pd.read_csv("datasets/students.csv")
#print (df)
#print (df.to_string())
#print(pd.options.display. max_rows)
#------------------------------


# Pandas Analyzing DataFrames#
#import pandas as pd
#data = pd.read_csv('datasets/students.csv')
#print(data.head(7))
#print(data.head()) # if head()is empty it will print first 5 rows of dataframe 
# tail() is used to print last rows and same as the head()
#print(data.tail())

#-----------------------------------------------
# now use for the data.csv 
#----------------------------------------------

"""import pandas as pd
df = pd.read_csv('datasets/data.csv')
new_df = df.dropna()
print(new_df.to_string)"""

#----------------- 
# remove all rows with null values
# ------------------------

"""import pandas as pd
df = pd.read_csv('datasets/data.csv')
df.dropna(inplace = True)
print(df.to_string)"""

#----------------- 
# replace null values with number 130
# ------------------------

import pandas as pd
df = pd.read_csv('datasets/data.csv')
#df.fillna(130, inplace = True)
df.fillna({"Calories":130}, inplace = True)

