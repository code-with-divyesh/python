class Student:
  def __init__(self,name): 
# The self parameter is a reference to the current
# instance of the class, and is used to access variables
# that belongs to the class.
    print("constructor is called")
    self.name=name
    print(self.name)

s1=Student("Divyesh")
