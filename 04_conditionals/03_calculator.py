# 04_calculator.py
# Simple calculator program in Python

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choose operation
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter your choice (+, -, *, /, %): ")

# Perform calculation
if choice == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
elif choice == "%":
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation selected!")
