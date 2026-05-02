# • Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.




class A:
    def display(self):
        print("A obj")
class B(A):
    def display(self):
        print("B obj")
        super().display()
class C(B):
    def display(self):
        super().display()
        print("Obj c")
obj=C()
obj.display()