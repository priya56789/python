# Q5. Create a class Temperature with:
# instance attribute celsius
# a static method to_fahrenheit(celsius)
# an instance method show_conversion() that uses the static method to print both values.


class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        fa=(celsius*9/5)+32
        print(fa)
    def show_conversion(self):
        print(self.celsius)
temp=Temperature(5)
Temperature.to_fahrenheit(22)
print(temp.celsius)