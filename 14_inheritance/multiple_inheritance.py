# First Parent Class
class Father:
    def father_name(self):
        print("Father: Samir")

# Second Parent Class
class Mother:
    def mother_name(self):
        print("Mother: Rekha")

# Child Class inherits from both Father and Mother
class Son(Father, Mother):
    def son_name(self):
        print("Son: Divyesh")

# create object of Child class
s1 = Son()

# access methods from both parents and child
s1.father_name()   # from Father
s1.mother_name()   # from Mother
s1.son_name()      # from Son
