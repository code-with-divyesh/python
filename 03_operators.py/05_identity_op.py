# identity_operators.py
# Program to demonstrate identity operators in Python

# Sample variables
x = [1, 2, 3]
y = x
z = [1, 2, 3]

# Identity checks
print("x is y ->", x is y)        # True because y references the same object as x
print("x is z ->", x is z)        # False because z is a different object
print("x is not z ->", x is not z) # True

# Using numbers (immutable objects)
a = 10
b = 10
print("a is b ->", a is b)        # True because small integers are cached
