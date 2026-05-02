# Q9. Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.



class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=self.amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            return False
holder1=BankAccount("Priyanka",1000)
holder2=BankAccount("Mani",2000)
BankAccount.change_bank_name("INDIAN")
print(BankAccount.bank_name)
print(holder1.bank_name)
print(BankAccount.validate_amount(100))
