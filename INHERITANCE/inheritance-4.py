# Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().


class Vehicle:
    def wheels(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
obj=Bike()
obj.wheels()
obj1=Car()
obj1.wheels()
obj2=Vehicle()
obj2.wheels()