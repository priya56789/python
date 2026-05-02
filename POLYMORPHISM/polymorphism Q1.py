# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().


class Animal:
    def make_sound(self):
        print("This is a Animal")
class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")
class Cat(Animal):
    def make_sound(self):
        print("Cat Meow Meow")
class Cow(Animal):
    def make_sound(self):
        print("amba amba")
Animals=[Dog(),Cat(),Cow()]
for A in Animals:
    A.make_sound()