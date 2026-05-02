# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states


class Student:
    def __init__ (self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,m):
        if 0<=m<=100:
            self.__marks=m
        else:
            print("Invalid")
s1=Student(80)
print(s1.get_marks())
s1.set_marks(89)
print(s1.get_marks())