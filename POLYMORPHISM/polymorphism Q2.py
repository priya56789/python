# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.


def operate(device):
    device.start()
class Car:
    def start(self):
        print("Car has 4 wheels")
class Computer:
    def start(self):
        print("Computer keyboard")
class washing_machine:
    def start(self):
        print("Clothes washing")
Objects=[Car(),Computer(),washing_machine()]
for O in Objects:
    O.start()
