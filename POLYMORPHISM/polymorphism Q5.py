# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.


class Payment:
    def process(self,amount):
        print(amount)
class CreditPayment(Payment):
    def process(self,amount,card_type):
        print(amount,card_type)
obj=Payment()
obj.process(10000)
obj1=CreditPayment()
obj1.process(20000,1000)

