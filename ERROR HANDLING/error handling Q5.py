#  Create a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        #self.balance-=amount
        if amount>self.balance:
            raise Exception("Invalid Balance")
        else:
            print("Transaction Successful")
acc=BankAccount(2900)
try:
    acc.withdraw(1500)
except Exception as e:
    print(e)
finally:
    print("Balance available")