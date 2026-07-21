# Program for Student Grading System

student_name = input("Enter the student's name: ")
marks = float(input("Enter the marks obtained by the student: "))

# Grade Calculation
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Pass / Fail
if marks >= 50:
    result = "Pass"
else:
    result = "Fail"

# Output
print("\n== STUDENT RESULT ==")
print("Student Name :", student_name)
print("Marks        :", marks)
print("Grade        :", grade)
print("Result       :", result)