#subjects = {"Math", "Science", "English", "History", "Geography", "Art", "Music", "Physical Education", "Computer Science", "Economics"} #in set we can store multiple values in a single variable and it is mutable also we use {} to define a set
#print(subjects)

#program 2 remove duplicate values from a list using set
#numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#unique_numbers = set(numbers)
#print(unique_numbers)

#//Program 3 - Add New values
#numbers = {1, 2, 3, 4, 5}
#numbers.add(6)
#print(numbers)

#//Program 4 - Remove Values
#numbers = {1, 2, 3, 4, 5}
#numbers.remove(3)
#print(numbers)

#//Program 5 - union of two sets
#set1 = {1, 2, 4, 5}
#set2 = {4, 5, 6, 8}
#union_set = set1.union(set2)
#print(union_set)

#//Program 6 - intersection of two sets
#set1 = {1, 2, 4, 5}
#set2 = {4, 5, 6, 8}
#intersection_set = set1.intersection(set2)
#print(intersection_set)

#//Practice Example:
colors = {"red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"}
print(colors)
print(colors.add("cyan"))
print(colors)
print(colors.remove("black"))
print(colors)
print(colors.union({"gray", "silver", "gold"}))
print(colors.intersection({"red", "green", "blue", "yellow"}))
print(colors.difference({"red", "green", "blue", "yellow"}))
print(colors.symmetric_difference({"red", "green", "blue", "yellow"}))
print(colors.isdisjoint({"red", "green", "blue", "yellow"}))
print(colors.issubset({"red", "green", "blue", "yellow"}))
print(colors.issuperset({"red", "green", "blue", "yellow"}))
print(colors.clear())
print(colors)
