class Student:
    school_name = "ABC School"   # class attribute

    def __init__(self, name):
        self.name = name         

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)



Student.show_school()
Student.change_school("XYZ School")
Student.show_school()
