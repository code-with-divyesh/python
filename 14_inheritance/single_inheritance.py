# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)   # call parent constructor
        self.roll_no = roll_no
        self.marks = marks

    def show_student_info(self):
        # call parent method
        self.show_details()
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# create object of Child class
s1 = Student("Divyesh", 20, 101, 95)

# call methods
s1.show_student_info()
