# membership_operators.py
# Program to demonstrate membership operators in Python

# Sample sequence
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

# Input from user
num = int(input("Enter a number to check in the list: "))
char = input("Enter a character to check in the string: ")

# Membership in list
print(f"{num} in list? ->", num in my_list)
print(f"{num} not in list? ->", num not in my_list)

# Membership in string
print(f"'{char}' in string? ->", char in my_string)
print(f"'{char}' not in string? ->", char not in my_string)
