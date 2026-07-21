#// 1. Positive, Negative, Zero Checker
#number = float(input("Enter a number: "))

#if number > 0:
    #print("Positive Number")
#elif number < 0:
    #print("Negative Number")
#else:
    #print("Zero")
#------------------------------------------------------------
#// 2. Largest Of Two Numbers
#num1 = float(input("Enter First Number:"))
#num2 = float(input("Enter Second Number:"))

#if num1 > num2:
    #print("Largest Number:", num1)
#elif num2 > num1:
    #print("Largest Number:", num2)
#else:
    #print("Both numbers are equal.")    
#-------------------------------------------------------------
#// 3. Smallest of Three Numbers
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

#if num1 <= num2 and num1 <= num3:
    #print("Smallest Number:", num1)
#elif num2 <= num1 and num2 <= num3:
    #print("Smallest Number:", num2)
#else:
    #print("Smallest Number:", num3)


#--------------------------------------------------------------------
# 4. Leap Year Checker
#year = int(input("Enter a year: "))

#if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    #print("Leap Year")
#else:
    #print("Not a Leap Year")

#-----------------------------------------------------
# 5. Vowel or Consonant
#letter = input("Enter a letter: ").lower()

#if letter in "aeiou":
    #print("Vowel")
#else:
    #print("Consonant")

#----------------------------------------------------------
# 6. Palindrome Checker
#word = input("Enter a word: ")

#if word == word[::-1]:
    #print("Palindrome")
#else:
    #print("Not a Palindrome")

#---------------------------------------------------
# 7. Count Vowels

#text = input("Enter a sentence: ").lower()

#count = 0

#for char in text:
    #if char in "aeiou":
        #count += 1

#print("Total Vowels:", count)

#--------------------------------------
# 7. Count Vowels

#text = input("Enter a sentence: ")

#words = text.split()

#for word in words:
    #print(word[::-1], end=" ")

#-----------------------------------------
# 9. Count Words

#text = input("Enter a sentence: ")

#words = text.split()

#print("Total Words:", len(words))

#---------------------------------------------------
# 10. Username Validator

#username = input("Enter username: ")

#if len(username) >= 5:
    #print("Valid Username")
#else:
    #print("Username is too short.")

#------------------------------------------
#11. Largest Number in List

#numbers = [10, 25, 4, 99, 8]

#print("Largest Number:", max(numbers))

#-----------------------------------
 #12. Smallest Number in List
#numbers = [10, 25, 4, 99, 8]

#print("Smallest Number:", min(numbers))

#-----------------------------------------
#13. Sum of List
#numbers = [5, 10, 20]

#print("Sum:", sum(numbers))

#-----------------------------------------

#14. Remove Duplicate Values
#numbers = [1, 2, 2, 3, 4, 4, 5]

#unique_numbers = list(set(numbers))

#print(unique_numbers)

#-------------------------------------

#15. Search an Item

#numbers = [10, 20, 30, 40, 50]

#search = int(input("Enter number to search: "))

#if search in numbers:
    #print("Number Found")
#else:
    #print("Number Not Found")

#------------------------------------
#16. Electricity Bill Calculator
#units = int(input("Enter electricity units: "))

#if units <= 100:
    #bill = units * 10
#elif units <= 200:
    #bill = units * 15
#else:
    #bill = units * 20

#print("Total Bill:", bill)

#---------------------------
# 17. Movie Ticket Price
#age = int(input("Enter your age: "))

#if age < 12:
    #price = 300
#elif age <= 60:
    #price = 500
#else:
    #price = 250

#print("Ticket Price:", price)

#--------------------------------------
#18. Login System
#username = input("Enter username: ")
#password = input("Enter password: ")

#if username == "admin" and password == "1234":
    #print("Login Successful")
#else:
    #print("Invalid Username or Password")

#-------------------------------------
#19. Number Guess Checker
#secret = 7

#guess = int(input("Guess the number: "))

#if guess == secret:
    #print("Correct Guess")
#elif guess > secret:
    #print("Too High")
#else:
    #print("Too Low")

#------------------------------------

#20. BMI Calculator

#weight = float(input("Enter weight (kg): "))
#height = float(input("Enter height (m): "))

#bmi = weight / (height * height)

#print("BMI:", round(bmi, 2))

#if bmi < 18.5:
    #print("Underweight")
#elif bmi < 25:
    #print("Normal Weight")
#elif bmi < 30:
    #print("Overweight")
#else:
    #print("Obese")

#------------------------------------------------------------------------------------------------------------------------