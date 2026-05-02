# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.


class Transport:
    def move(self):
        print("Transport charge")
class Bus(Transport):
    def move(self):
        print("Bus crowd")
        super().move()
class Bike(Bus):
    def move(self):
        print("Bike pleasant")
object=[Bus(),Bike()]
for o in object:
    o.move()