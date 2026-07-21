
#------------------
# Practice 1. Table of 2 (Hardcoded)

#print("Multiplication Table of 2")

#for i in range(1, 11):
    #print(f"2 x {i} = {2 * i}")

#---------------------------------
# Practice 2. User Input

#number = int(input("Enter a number: "))

#print(f"\nMultiplication Table of {number}")

#for i in range(1, 11):
    #print(f"{number} x {i} = {number * i}")

#---------------------------------
# Practice 3. While Loop Version

#number = int(input("Enter a number: "))

#count = 1

#while count <= 10:
    #print(f"{number} x {count} = {number * count}")
    #count += 1

#---------------------------
# Practice 4. Tables from 1 to 5

for table in range(1, 6):
    print(f"\nTable of {table}")

    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")