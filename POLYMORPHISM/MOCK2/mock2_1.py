class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        self.__balance-=amount
