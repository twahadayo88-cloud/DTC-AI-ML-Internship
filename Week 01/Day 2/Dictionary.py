#//Program 1 to create a dictionary

#student = {
    #"name": "Muhammad Twaha",
    #age": 23,
    #"University": "SZABIST",
    #"Major": "Computer Science"
#}
#print(student)

#//Program 2 - Access Values
#student = {
    #"name": "Muhammad Twaha",
    #"age": 23,
    #"University": "SZABIST",
    #"Major": "Computer Science"
#}
#print(student["name"])
#print(student["age"])
#print(student["University"])

#//Program 3 - Add New Data
#student = {
    #"name": "Muhammad Twaha",
    #"age": 23,
    #"University": "SZABIST",
    #"Major": "Computer Science"
#}
#address = "Karachi"
#student["address"] = address
#print(student)

#//Program 4 - Update Data
#student["age"] = 24
#print(student)

#program 5 - Delete Data
#student = {
    #"name": "Muhammad Twaha",
    #"age": 23,
    #"University": "SZABIST",
    #"Major": "Computer Science"
#}
#del student["age"]
#print(student)

#// practice example
employee = {
    "name": "Asfand Ali",
    "age": 40,
    "position": "Software Developer",
    "department": "IT",
    "salary": 80000
}
print(employee)
print(employee["name"])
print(employee["age"])
print(employee["position"])
print(employee["department"])
print(employee["salary"])
remove_key = "salary"
del employee[remove_key]
print(employee)