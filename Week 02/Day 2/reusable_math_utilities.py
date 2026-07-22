# --------"Practical Task of these concepts"

# Addition Function
def add(a, b):
    return a + b


# Subtraction Function
def subtract(a, b):
    return a - b


# Multiplication Function
def multiply(a, b):
    return a * b


# Division Function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Square Function
def square(number):
    return number * number


# Cube Function
def cube(number):
    return number * number * number

print("===== Reusable Math Utility =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Cube")
print("7. Exit")

choice = int(input("\nEnter your choice (1-7): "))

    # Addition
if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add(num1, num2)
        print("Result =", result)

    # Subtraction
elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = subtract(num1, num2)
        print("Result =", result)

    # Multiplication
elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = multiply(num1, num2)
        print("Result =", result)

    # Division
elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = divide(num1, num2)
        print("Result =", result)

    # Square
elif choice == 5:
        number = float(input("Enter a number: "))

        result = square(number)
        print("Result =", result)

    # Cube
elif choice == 6:
        number = float(input("Enter a number: "))

        result = cube(number)
        print("Result =", result)

    # Exit
elif choice == 7:
        print("\nThank you for using Math Utility Program.")

    # Invalid Choice
else:
        print("\nInvalid Choice! Please select between 1 and 7.")