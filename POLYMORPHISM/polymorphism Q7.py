# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.


class Account:
    def withdraw(self):
        print("Amount to pay")
class Savings_account(Account):
    def withdraw(self):
        print("Savings Account")
class PremiumSavingsAccount(Savings_account):
    def withdraw(self):
        super().withdraw()
        print("Premium Account")
obj=Account()
obj.withdraw()
ob=Savings_account()
ob.withdraw()
obj1=PremiumSavingsAccount()
obj1.withdraw()

