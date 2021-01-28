"""
class
object
inheritance
polymorphism
Abstaction
Encapsulation
"""
#1.Class [Collection of methods, variables]
"""
class Test:
    def show(self):
        print("i am in Class Test.")
t=Test()
t.show()
"""
#2.Object [class object could be used to access different attributes.]
# [It can also be used to create new object instances (instantiation) of that class]
"""
t=Test()
t.show()
"""
# Constructor
#__init__ we can able to called as constructor method.
#whenever objects is created by default init it will call
"""
class Student:
    college = "YV University"
    location = "Kadapa"

    def __int__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("i am in __init__")
    def getfullname(self):
        return f'{self.fname} {self.lname}'
"""
#Self [self is a Binding Object.]
#Be using self we can able to call methods and variables

# Encapsulation



















