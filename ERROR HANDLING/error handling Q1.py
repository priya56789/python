# Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.



class Person:
    def __init__(self,age):
        self.age=age
        if age<0:
            raise ValueError("Age cannot be negative")
try:
    obj=Person(-25)
except ValueError as ve:
    print(ve)
finally:
    print("Execution completed")
