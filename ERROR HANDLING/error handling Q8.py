#  Create a base class Shape with a method area() that raises
# NotImplementedError. Create a child class Rectangle that overrides and
# implements the area method.


class shape():
    def area(self):
        raise NotImplementedError("Method is not implemented")
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)
obj1=Rectangle(5,4)
obj=shape()
try:
    obj1.area()
    obj.area()
except NotImplementedError as ne:
    print(ne)
finally:
    print("execution complete")

