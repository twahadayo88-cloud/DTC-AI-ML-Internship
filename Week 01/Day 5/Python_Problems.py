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

#// 3. Smallest of Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest Number:", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest Number:", num2)
else:
    print("Smallest Number:", num3)
