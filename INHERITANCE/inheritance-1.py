# Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.

class  Animal:
    def sound(self):
        print("Animal is Animal")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        super().sound()
obj=Dog()
obj.sound()

