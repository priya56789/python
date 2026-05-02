# 1. Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.
# Demonstrate:
# • Polymorphic behavior by iterating through all account types
# • Preventing direct access to balance
# • Multiple interest strategies

from abc import ABC, abstractmethod
class Account(ABC):
    interest = 1
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
    @classmethod
    # @abstractmethod
    def change_interest(cls,new_interest):
        cls.interest = new_interest
    @staticmethod
    def validate_balance(balance):
        if balance < 0:
            return False
        return True
    @property
    def get_balance(self):
        return self.__balance
    @get_balance.setter
    def get_balance(self, amount):
        self.__balance = amount
    def __str__(self):
        return f'{self.name} balance: {self.get_balance}'
    def __repr__(self):
        return f'({self.name} balance: {self.get_balance})'

class SavingsAccount(Account):
    interest=0.1
    def __init__(self, name, balance):
        super().__init__(name,balance)
    @classmethod
    def change_interest(cls,new_interest):
        cls.interest=new_interest
    def deposit(self, amount):
        if self.validate_balance(amount):
            self.get_balance += amount
        else:
            print( " Invalid deposit")

    def withdraw(self, amount):
        if self.validate_balance(amount):
            if amount > self.get_balance:
                self.get_balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid withdrawal")

    def calculate_interest(self):
        self.get_balance += self.interest


class CurrentAccount(Account):
    interest=0.05
    def __init__(self, name, balance):
        super().__init__(name,balance)

    def deposit(self, amount):
        if self.validate_balance(amount):
            self.get_balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if self.validate_balance(amount):
            if amount <= self.get_balance:
                self.get_balance -= amount
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Withdrawal")

    def calculate_interest(self):
        self.get_balance += self.get_balance * self.interest / 2

    @classmethod
    def change_interest(cls, interest):
        cls.interest = interest
class FixedDepositAccount(Account):
    interest=0.12
    def __init__(self, name, balance):
        super().__init__(name,balance)

    @classmethod
    def change_interest(cls, interest):
        cls.interest = interest

    def deposit(self, amount):
        if self.validate_balance(amount):
            self.get_balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        print("Cannot withdraw from fixed Deposit.")


    def calculate_interest(self):
        self.get_balance += self.get_balance * self.interest

ac1=SavingsAccount("Priyanka", 50000)
acc2=CurrentAccount("Bhavana", 800000)
acc3 = FixedDepositAccount("Anjali",60000)
l=[ac1,acc2,acc3]
# print(l)
for i in l:
    print(l)
    i.deposit(1000)
    i.withdraw(2000)
    i.calculate_interest()
    print("After Operations: ", l)
# # # print(l)
SavingsAccount.change_interest(0.6)
print("Bank-wide interest rate updated to:",SavingsAccount.interest)

CurrentAccount.change_interest(0.7)
print("Bank-wide interest rate updated to:",CurrentAccount.interest)

FixedDepositAccount.change_interest(0.8)
print("Bank-wide interest rate updated to:",FixedDepositAccount.interest)

# Account.change_interest(2)
# print(Account.interest)