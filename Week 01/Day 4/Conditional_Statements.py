
#// programs for conditnal statements

#//if Statement
age = 18
if age >= 18:
    print("You are eligible for Government Job.")

#//if-else Statement
age = 17
if age >= 18:
    print("You are eligible for Government Job.")
else:
    print("You are not eligible for Government Job.")


#//if-elif-else Statement
# // program to check the grade of a student based on marks
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


#//Nested if Statement
age = 20
license = True
if age >= 18:
    if license:
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")


    #//Logical Opertors with Conditions
    age = 25
    if age >= 18 and age <= 60:
        print("You are eligible for Government Job.")