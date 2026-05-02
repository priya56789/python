# 3. Create:
# • Abstract class PaymentMethod with pay(), validate()
# • Subclasses: CardPayment, WalletPayment, UPIPayment
# • Encapsulate user balance
# • Use @property to control reading available funds
# • Overload + operator to combine two payment methods into “split payment”
# • Demonstrate polymorphism through a checkout loop.

from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    def __init__(self,balance):

        self.__balance = balance

    @property
    def get_bal(self):
        return self.__balance
    @get_bal.setter
    def get_bal(self,amount):
        if amount < 0:
            print("Amount Not valid")
        else:
            self.__balance = amount

    def _deduct(self,amount):
        self.get_bal -= amount

    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def validate(self):
        pass

    def __add__(self, other):
        # if not isinstance(other, PaymentMethod):
        #     raise TypeError("Can only combine PaymentMethod objects")
        return SplitPayment(self, other)
class CardPayment(PaymentMethod):
    def validate(self):
        return True

    def pay(self,amount):
        if self.get_bal >= amount:
            self._deduct(amount)
            print("Paid using Card")
        else:
            print("Not enough balance in card")
    def __str__(self):
        return "Card"
    # def __add__(self,other):
    #     print(f"paying through {self} and {other}")

class WalletPayment(PaymentMethod):
    def validate(self):
        return True
    def pay(self,amount):
        if self.get_bal >= amount:
            self._deduct(amount)
            print("Paid Using Wallet")
        else:
            print("Not enough balance in wallet")
    def __str__(self):
        return "Wallet"
    # def __add__(self,other):
    #     print(f"paying through {self} and {other}")
class UPIPayment(PaymentMethod):
    def validate(self):
        return True
    def pay(self,amount):
        if self.get_bal >= amount:
            self._deduct(amount)
            print("Paid using UPI")
        else:
            print("Not enough balance in UPI")
    def __str__(self):
        return "UPI"
    # def __add__(self,other):
    #     print(f"paying through {self} and {other}")
class SplitPayment:
    def __init__(self,pay1,pay2):
        self.method1=pay1
        self.method2=pay2
    def pay(self,amount):
        print(f"paying {amount}...")
        deduct_amt = amount//2
        self.method1.pay(deduct_amt)
        self.method2.pay(deduct_amt)
        print(f"{deduct_amt} is deducted from the {self.method1} ,remaining balance in {self.method1} is {self.method1.get_bal}")
        print(f"{deduct_amt} is deducted from the {self.method2},remaining balance in {self.method2} is {self.method2.get_bal}")

card = CardPayment(1000)
wallet = WalletPayment(2000)
upi = UPIPayment(3000)
splits=card+upi
splits.pay(1500)

# payments = [card,wallet,upi]
# for methods in payments:
#     methods.pay(500)
#     print()
# print(.get_bal)