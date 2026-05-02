# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.


class Vector:
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    def __add__ (self,other):
        return (self.a+other.a,self.b+other.b)
    def __eq__ (self,other):
        return self.a==other.a and self.b==other.b
v1=Vector(2,3)
v2=Vector(3,5)
v3=v1+v2
print(v3)
print(v1==v2)
