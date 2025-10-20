# class Student:
#     name = "Divyesh"
#     age = 20
#     course = "MCA"

# # creating object
# s1 = Student()

# # accessing data using object
# print(s1.name)
# print(s1.age)
# print(s1.course)


# class attribute and instance att

class Student:
    college = "ABC College"  # class attribute

# creating objects
s1 = Student()
s2 = Student()

# adding instance attributes
s1.name = "Divyesh"
s1.age = 20

s2.name = "Raj"
s2.age = 21

print(s1.name, s1.age, s1.college)
print(s2.name, s2.age, s2.college)
