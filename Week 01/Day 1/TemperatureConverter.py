def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    f = (c * 9/5) + 32
    return f

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    c = (f - 32) * 5/9
    return c

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin"""
    k = c + 273.15
    return k

# User se input le
print("=== Temperature Converter ===")
temp = float(input("Enter temperature: "))
unit = input("Convert from (C/F/K): ").upper()

if unit == "C":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
elif unit == "F":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    print(f"{temp}°F = {celsius_to_kelvin(fahrenheit_to_celsius(temp)):.2f}K")
elif unit == "K":
    print(f"{temp}K = {temp - 273.15:.2f}°C")
    print(f"{temp}K = {celsius_to_fahrenheit(temp - 273.15):.2f}°F")
else:
    print("Invalid unit! Use C, F, or K")