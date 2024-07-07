# OOPS In python
# class Students:
#     name = "Tsnmsy"

# s1 = Students()
# print(s1)

# class Car:
#     color = "white"
#     brand = "RTC"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     print("Inside Class")
#     name = "sbffbsfbsfb"
#     # Default COnstructor
#     def __init__(self):
#         print("Inside Constructor.....")
#         self.name = name

#     # Parameterized Constructor
#     def __init__( self, name):
#         print("Inside Constructor.....")
#         self.name = name

#     def hello(self):
#         print("Hello.....")

#     def getName(self):
#         return self.name

# s1 = Student("Tanmay Raut")
# print(s1.name)
# s1.hello()
# print(s1.getName())

# We can write anything instead of self like we can also write this also,
# but because of naming convention we write self as most of python programmer prefer to use self

# Que 1. Create a class of Student that takes name and marks of3 subjects as a arguments in constructor.
# class Students:
#     def __init__(self, maths, phy, chem):
#         self.maths = maths
#         self.phy = phy
#         self.chem = chem

#     def avg(self):
#         return (self.maths+ self.phy+ self.chem)/3
    
# s1 = Students(98,94,97)
# print(s1.avg())


# Que 2.  Create a Bnak Account Class
class Bank:
    balance = 0
    
    def __init__(self, name, accNo):
        self.name = name
        self.accNo = accNo

    def 