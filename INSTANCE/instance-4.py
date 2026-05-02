# Q4. Create a class Car with:
# instance attribute mileage
# class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.



class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display(self):
        print(self.mileage)
        print(self.wheels)
    @classmethod
    def change_wheels(cls,new_wheelsno):
        cls.wheels=new_wheelsno
obj1=Car(8)
Car.change_wheels("5")
print(Car.wheels)
print(obj1.mileage)