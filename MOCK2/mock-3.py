'''from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    def __init__(self,balance):
        self.__balance = balance
    @property
    def get_bal(self):
        return self.__balance
    @get_bal.setter
    def get_bal(self,amount):
            self.__balance = amount
    def deduct(self,amount):
        self.get_bal -= amount
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def validate(self,amount):
        pass
    def __add__(self, other):
        return SplitPayment(self, other)
class CardPayment(PaymentMethod):
    def validate(self,amount):
        return True
    def pay(self,amount):
        if self.get_bal >= amount:
            self.deduct(amount)
            print("Paid using Card")
        else:
            print("balance not sufficient")
    def __str__(self):
        return "Card"

class WalletPayment(PaymentMethod):
    def validate(self,amount):
        return True
    def pay(self,amount):
        if self.get_bal >= amount:
            self.deduct(amount)
            print("Paid Using Wallet")
        else:
            print("balance not sufficient")
    def __str__(self):
        return "Wallet"

class UPIPayment(PaymentMethod):
    def validate(self,amount):
        return True
    def pay(self,amount):
        if self.get_bal >= amount:
            self.deduct(amount)
            print("Paid using UPI")
        else:
            print("balance not sufficient")
    def __str__(self):
        return "UPI"

class SplitPayment:
    def __init__(self,p1,p2):
        self.method1=p1
        self.method2=p2
    def pay(self,amount):
        deduct_amt = amount//2
        self.method1.pay(deduct_amt)
        self.method2.pay(deduct_amt)
        print(f"{deduct_amt} is deducted from the {self.method1} ,remaining balance in {self.method1} is {self.method1.get_bal}")
        print(f"{deduct_amt} is deducted from the {self.method2},remaining balance in {self.method1} is {self.method1.get_bal}")
card = CardPayment(800)
upi=UPIPayment(100)
wallet=WalletPayment(3000)
splits=card+upi
splits.pay(800)
payments=[card,upi,wallet]
for p in payments:
    p.pay(2000)
    print()'''


'''from abc import ABC,abstractmethod
class Menuitem(ABC):
    @abstractmethod
    def get_price(self):
        pass
class Pizza(Menuitem):
    def __init__(self,size):
        self.size=size
    def get_price(self):
        if self.size=="small":
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
            return 20
        elif self.size=="Medium":
            return 50
        else:
            return 70
class Order:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def total_price(self):
        total=0
        for item in self.items:
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


from abc import ABC,abstractmethod
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
        return self.__quantity
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
        self.products={Product}
        Warehouse.total_warehouses+=1
    def add_product(self,product):
        if product in self.products:
            return product.get_quantity
        else:
            return "None"
    def __add__(self, other):
        return self.name+other.name
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
w1=Warehouse("Bhavana")
w2=Warehouse("Anjali")
w3=w1+w2
print(w1.__add__(w2))






















