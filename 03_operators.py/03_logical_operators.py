# Program to demonstrate logical operators in Python

# Take input from user
a = bool(int(input("Enter 0 for False, 1 for True for a: ")))
b = bool(int(input("Enter 0 for False, 1 for True for b: ")))

# Logical AND
print(f"{a} and {b} =", a and b)

# Logical OR
print(f"{a} or {b} =", a or b)

# Logical NOT
print(f"not {a} =", not a)
print(f"not {b} =", not b)
