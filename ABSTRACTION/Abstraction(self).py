'''from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,balance):
        self.__balance=balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def calculate_interest(self,amount):
        pass
    @staticmethod
    def is_valid(amount):
        if amount>0:
            return True
        return False
    def set_balance(self,balance):
        self.__balance+=balance
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"balance:{self.__balance}"
    def __repr__(self):
        return f"balance:{self.__balance}"
    @classmethod
    def change_interest(cls,new):
        pass
class SavingsAccount(Account):
    interest_rate=0.1
    def __init__(self,balance):
        super().__init__(balance)
    @classmethod
    def change_interest(cls,new):
        cls.interest_rate=new
    def deposit(self,amount):
        self.set_balance(amount)
    def withdraw(self,amount):
        self.set_balance(-amount)
    def calculate_interest(self):
       self.get_balance()*self.interest_rate+10000
       return
class CurrentAccount(Account):
    interest_rate=0.5
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.set_balance(amount)
    def withdraw(self,amount):
        self.set_balance(-amount)
    def calculate_interest(self):
        self.get_balance()*self.interest_rate+10000
        return
    @classmethod
    def change_interest(cls,new):
        cls.interest_rate=new
acc1=SavingsAccount(80000)
acc2=CurrentAccount(140000)
Account=[acc1,acc2]
for i in Account:
    i.deposit(200)
    i.withdraw(800)
    i.calculate_interest()
    print(i.get_balance())
    print(i.__str__())'''


'''from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self):
        pass
class Car(Vehicle):
    base_price=300
    def __init__(self):
        print("Ride on car")
        self.price_per_km=30
class  Bike(Vehicle):
    base_price=100
    def __init__(self):
        print("Bike ride")
        self.price_per_km=10
class Auto(Vehicle):
    base_price=200
    def __init__(self):
        print("Ride on Auto")
        self.price_per_km=20
class Driver:
    def __init__(self,vehicle):
        self.vehicle=vehicle
        print("Driver started the vehicle")
class Ride:
    def __init__(self,driver):
        print("By vehicle driver goes to ride")
        self.driver=driver
    def __calculate_fair(self,km):
        print(f"calculating fair for {km} kms")
        total=self.driver.vehicle.price_per_km+km*self.driver.vehicle.base_price
        return total
    def get_price(self,km):
        return self.__calculate_fair(km)
obj=Ride(Driver(Auto()))
print(obj.get_price(20))'''




'''from abc import ABC,abstractmethod
class Paymentmethod(ABC):
    def __init__(self,balance):
        self.__balance=balance
    @property
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")     
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def validate(self,amount):
        pass
    def __add__(self,other):
        return SplitPayment(self,other)
def cardpayment(Paymentmethod):
    def __init__(self,balance):
        super().__init__(balance)
    def pay(self,amount):
        self.get_balance(amount)
    def validate(self,amount):
        return True
class WalletPayment(Paymentmethod):
    def __init__(self,balance):
        super().__init__(balance)
    def pay(self,amount):
        self.get_balance(amount)
    def validate(self,amount):
        return True
class UPIPayment(Paymentmethod):
    def __init__(self, balance):
        super().__init__(balance)
    def pay(self, amount):
        self.get_balance(amount)
    def validate(self, amount):
        return True
o1=CardPayment(2000)
o2=UPIPayment(3000)
l=[o1,o2]
for i in l:
    i.pay(200)
    i.validate(300)'''

'''from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary
    @abstractmethod
    def perform_duty(self):
        pass
    @property
    def  get_salary(self):
        return self.__salary
    @get_salary.setter
    def get_salary(self,salary):
        self.__salary=salary
    def __str__(self):
        return f" Vasundhara salary is {self.__salary}"
    def __repr__(self):
        return f" Rishika salary is {self.__salary}"
class MedicalStaff(Person):
    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department
    def display(self):
        return self.get_salary
    def perform_duty(self):
        return f"{self.name} doing medical responsibilities"
class Doctor(MedicalStaff):
    def __init__(self,name,age,salary,department,specilization):
        super().__init__(name,age,salary,department)
        self.specilization=specilization
    def perform_duty(self):
        return f"{self.name} is performing surgery"
class  Surgeon(Doctor):
    def __init__(self,name,age,salary,department,specilization,patient_notes):
        super().__init__(name,age,salary,department,specilization)
        self.__patient_notes=patient_notes
    def perform_duty(self):
        return f"{self.name} is going to do surgery"
    def get_patient_notes(self):
        return "Patient details"
obj=Doctor("priya",21,210000,"Cardiologist","cardio")
obj1=MedicalStaff("Anjali",20,20000,"medicalstore")
print(obj1.get_salary)
print(obj1.__str__())
obj2=Surgeon("Pravallika",22,200000,"surgical","surgeon","plastic_surgery")
Staff=[obj,obj1,obj2]
for member in Staff:
    print(member.perform_duty())'''


'''class User:
    def __init__(self,name,course):
        self.name=name
        self.__course=course
    def get_course(self):
        return self.__course
class Instructor(User):
    def grade_work(self):
        pass
    def submit_work(self):
        pass
class Student(User):
    def grade_work(self):
        pass
    def submit_work(self):
        pass
class TeachingAssistant(Student,Instructor):
    def grade_work(self):
        print("A grade")
    def submit_work(self):
        print("Work done")
obj=TeachingAssistant("Priyanka","Python")
obj.grade_work()
obj.submit_work()
print(obj.get_course())
print(TeachingAssistant.__mro__)'''


'''from abc import ABC
class Product(ABC):
    def __init__(self,name,price,quantity):
        self.name=name
        self.__price=price
        self.__quantity=quantity
    @property
    def get_price(self):
        return self.__price
    @property
    def get_quantity(self):
        return self.__quality
    @get_price.setter
    def get_price(self,price):
        if price>0:
            self.__price+=price
        else:
            print("No price")
    @get_quantity.setter
    def get_quantity(self,price):
        if price>0:
            return True
        return False
    def __str__(self):
        return f"price:{self.__price},quantity:{self.__quantity}"
class Warehouse(Product):
    total_warehouses=0
    def __init__(self,name):
        self.name=name
        self.products={}
        Warehouse.total_warehouses+=1
    def add_product(self,product):
        if product in self.products:
            return product.get_quantity
        else:
            return "None"
    def __add__(self, other):
        print(self.name+other.name)
    def __len__(self):
        return len(self.products)
    def __contains__(self, item):
        return item in self.products
    @classmethod
    def total_warehouse(cls):
       return cls.total_warehouses
P1=Product("A",10,2)
P2=Product("B",20,3)
P3=Product("C",30,4)
w1=Warehouse("Priya")
w2=Warehouse("Anjali")
w3=w1+w2
print(w1.__add__(w2))'''



'''from abc import ABC,abstractmethod
class MediaFile(ABC):
    def __init__(self,file_name):
        self.__file_name=file_name
    @property
    def get_file(self):
        return self.__file_name
    def validation(self):
        return self.get_file()>0
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3File(MediaFile):
    def play(self):
        return f" MP3File has name{self.get_file}"
    def stop(self):
        return f"MP3File {self.get_file} has stopped"
class MP4File(MediaFile):
    def play(self):
        return f" MP4File has name{self.get_file}"
    def stop(self):
        return f"MP4File {self.get_file} has stopped"
class WAVFile(MediaFile):
    def play(self):
        return f" WAVFile has name{self.get_file}"
    def stop(self):
        return f"WAVFile {self.get_file} has stopped"
def start_player(media):
    print(media.play())
mp3=MP3File("Songs")
mp4=MP4File("Youtube")
WAV=WAVFile("netflix")
media=[mp3,mp4,WAV]
for i in media:
    print(i.play())
    print(i.stop())'''



'''from abc import ABC,abstractmethod
class StatementFormatter(ABC):
    @abstractmethod
    def formatter(self,data):
        pass
    def __call__(self,data):
        return self.formatter(data)
    def __repr__(self):
        return self.formatter(data)
class PDFFormatter(StatementFormatter):
    def formatter(self,data):
        return f"PDF:{data}"
class JSONFormatter(StatementFormatter):
    def formatter(self,data):
        return f"JSON:{data}"
class TextFormatter(StatementFormatter):
    def formatter(self,data):
        return f"text format:{data}"
data={"name:Priya","age=21"}
formatters=[PDFFormatter(),JSONFormatter(),TextFormatter()]
for f in formatters:
    print(f.formatter(data))'''



'''from abc import ABC,abstractmethod
class Menuitem(ABC):
    @abstractmethod
    def get_price(self):
        pass
class Pizza(Menuitem):
    def __init__(self,size):
        self.size=size
    def get_price(self):
        if self.size=="Small":
            return 200
        elif self.size=="Medium":
            return 300
        else:
            return 400
class Burger(Menuitem):
    def __init__(self,cheese):
        self.cheese=cheese
    def get_price(self):
        price=150
        if self.cheese:
            price+=30
        return price
class Drink(Menuitem):
    def __init__(self,size):
        self.size=size
    def get_price(self):
        if self.size=="small":
            return 30
        elif self.size=="medium":
            return 50
        else:
            return 70
class Order:
    def __init__(self):
        self.__items=[]
    def add_item(self,item):
        self.__items.append(item)
    def total_price(self):
        total=0
        for item in self.__items:
            total+=item.get_price()
        return total
o=Order()
p=Pizza("Medium")
b=Burger(True)
d=Drink("Large")
o.add_item(p)
o.add_item(b)
o.add_item(d)
print(o.total_price())'''



