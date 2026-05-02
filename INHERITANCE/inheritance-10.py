# Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor.


class Person:
    def __init__ (self,name):
        self.name=name
class Student(Person):
    def __init__ (self,name,roll_no):
        super().__init__(name)
        self.roll_no=roll_no
obj=Student("Anjali",34)
print(f"Object:{obj.name},Roll:{obj.roll_no}")


