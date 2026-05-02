# 1. Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.


class BankAccount:
    def __init__ (self,Account_number,balance):
        self.Account_number=Account_number
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def withdraw(self,amount):
        if 0<=amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Invalid Input")
    @property
    def get_balance(self):
        return self.__balance
obj=BankAccount(123,30000)
obj.deposit(3000)
print(obj.get_balance)
obj.withdraw(200)
print(obj.get_balance)