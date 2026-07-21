
#// Utility 1 → Age Calculator
print("== AGE CALCULATOR ==")

birth_year = int(input("Enter your birth year: "))

current_year = 2026

age = current_year - birth_year

print("Your Age is:", age)

#// Utility 2 → Even Odd Checker
print("\n== EVEN ODD CHECKER ==")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#// Utility 3 → Password Checker
print("\n== PASSWORD CHECKER ==")

password = input("Enter Password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")


#// Utility 4 → Character Counter
print("\n== CHARACTER COUNTER ==")

text = input("Enter a sentence: ")

print("Total Characters:", len(text))