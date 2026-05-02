# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?


def draw(shape):
    shape.draw()
class Circle:
    def draw(self):
        print("Circular Object")
class  Square:
    def draw(self):
        print("Square table")
class Rectangle:
    def draw(self):
        print("Rectangular table")
object=[Circle(),Square(),Rectangle()]
for o in object:
    o.draw()