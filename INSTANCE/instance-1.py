# Create an abstract class Shape with an abstract method area(). Create class
# Rectangle(Shape) that implements the area() method.


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
        return False
s1=student("priyanka",40)
s2=student("Eswar",55)
print(s1.is_passed())
print(s2.is_passed())