# Grandparent Class
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

    def show_grandfather(self):
        print("Grandfather Name:", self.grandfather_name)


# Parent Class (inherits from Grandfather)
class Father(Grandfather):
    def __init__(self, grandfather_name, father_name):
        super().__init__(grandfather_name)  # call Grandfather constructor
        self.father_name = father_name

    def show_father(self):
        print("Father Name:", self.father_name)


# Child Class (inherits from Father)
class Son(Father):
    def __init__(self, grandfather_name, father_name, son_name):
        super().__init__(grandfather_name, father_name)  # call Father constructor
        self.son_name = son_name

    def show_son(self):
        print("Son Name:", self.son_name)


# creating object of last class
s1 = Son("krishnakant", "samir", "Divyesh")

# showing full family details
s1.show_grandfather()
s1.show_father()
s1.show_son()
