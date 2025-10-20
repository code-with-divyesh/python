# class Student:
#   def __init__(self,name): 
#     print("constructor is called")
#     self.name=name
#   def Display(self):
#     print(self.name)

# s1=Student("Divyesh")
# s1.Display()

# practice question

class Student:
    def __init__(self, name, marks):
        self.name = name             # ✅ assign name correctly
        self.marks = marks

    def Average_marks(self):
        total = 0                    # ✅ initialize sum variable
        for val in self.marks:
            total += val
        avg = total / len(self.marks)  # ✅ dynamic average
        print("Name:", self.name)
        print("Average Marks:", avg)

# create object and call method
s1 = Student("Divyesh", [98, 97, 90])
s1.Average_marks()


