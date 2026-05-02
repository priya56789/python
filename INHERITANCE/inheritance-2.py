# Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super()

class A:
    def show(self):
        print("obj A")
class B(A):
    def show(self):
        print("Obj B")
        super().show()
obj=B()
obj.show()

