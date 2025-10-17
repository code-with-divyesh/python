# 05_string_operations.py
# Simple program for basic string operations

# Take input from user
text = input("Enter any string: ")

# Display original string
print("Original String:", text)

# String length
print("Length of string:", len(text))

# Change case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# String slicing
print("First 3 letters:", text[:3])
print("Last 3 letters:", text[-3:])
print("Reversed string:", text[::-1])

# Count and find
ch = input("Enter a character to count: ")
print(f"'{ch}' occurs {text.count(ch)} times in the string.")
print(f"First position of '{ch}':", text.find(ch))

# Replace example
new_text = text.replace(" ", "_")
print("After replacing spaces with underscores:", new_text)
