# Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100.

class Student:
    #def __init__(self,marks):
        #self.marks=marks
        #print(self.marks.;)
    def set_marks(self,marks):
        if marks<0 or marks>100:
            raise ValueError("marks cannot be negative")
    def __str__(self):
        return f"marks:{self.marks}"
obj=Student()
try:
    obj.set_marks(120)
except ValueError as ve:
    print(ve)
finally:
    print("Execution Completed")