# Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.


class Sorter:
    def change(self,strategy):
        self.strategy=strategy
    def sort(self):
        self.strategy.logic()
class BS:
    def logic(self):
        print("Bubble Sort")
class MS:
    def logic(self):
        print("Merge Sort")
class QS:
    def logic(self):
        print("Quick Sort")
obj=Sorter()
obj.change(BS())
obj.sort()
obj1=Sorter()
obj1.change(MS())
obj1.sort()
obj2=Sorter()
obj2.change(QS())
obj2.sort()
