# 2. Build:
# • Vehicle base class
# • Car, Bike, Auto subclasses
# • A Driver class that contains a Vehicle
# • A Ride class that:
# o Calculates fare differently depending on the type of vehicle (polymorphism)
# o Stores driver + vehicle combination
# o Protects internal fare formula through encapsulation
# Also:
# • Use __str__ to print readable ride summaries.
# Show how composition + polymorphism interact.

from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,name,no):
        self.vehicle_name=name
        self.vehicle_no=no
        self.base_rate=100
    @abstractmethod
    def calculate_fare(self,distance):
        pass
    @abstractmethod
    def __str__(self):
        pass
class Car(Vehicle):
    # def __init__self(self,name,no):
    #     super().__init__(name,no)

    def calculate_fare(self,distance):
        service_fee = 100
        return self.base_rate * distance + service_fee

    def __str__(self):
        return f"vehicle_type:Car,vehicle_name:{self.vehicle_name},vehicle_no:{self.vehicle_no}"

class Bike(Vehicle):
    # def __init__self(self,name,no):
    #     super().__init__(name,no)
    def calculate_fare(self,distance):
        return self.base_rate * distance
    def __str__(self):
        return f"vehicle_type:Bike,vehicle_name:{self.vehicle_name},vehicle_no:{self.vehicle_no}"

class Auto(Vehicle):
    # def __init__self(self,name,no):
    #     super().__init__(name,no)
    def calculate_fare(self,distance):
        return self.base_rate*distance+10
    def __str__(self):
        return f"vehicle_type:Auto,vehicle_name:{self.vehicle_name},vehicle_no:{self.vehicle_no}"

class Driver:
    def __init__(self,name,vehicle):
        self.name = name
        self.vehicle = vehicle

    def __str__(self):
        return f"Driver: {self.name},Vehicle: {self.vehicle}"

class Ride :
   def __init__(self,driver,distance):
       self.driver = driver
       self.__distance = distance
   def calculate_fare(self):
       return self.driver.vehicle.calculate_fare(self.__distance)

   def __str__(self):
       return (f"Ride Summary:\nDriver: {self.driver.name}\n"
               f"Vehicle: {self.driver.vehicle}\n"
               f"Distance: {self.__distance}\n"
               f"Fare: {self.calculate_fare()}")



car=Car("shift",1245)
bike=Bike("pulsar",1502)
auto=Auto("bajaj",1475)

driver1=Driver("anil",car)
driver2=Driver('chandra',bike)
driver3=Driver('ramesh',auto)

ride1=Ride(driver1,50)
ride2 = Ride(driver2,40)
ride3 = Ride(driver3,30)

print(ride1)
print("---")
print(ride2)
print("---")
print(ride3)