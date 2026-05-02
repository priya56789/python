# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.



class UPI:
    def pay(self):
        print("UPI PIN")
class Card:
    def pay(self):
        print("SBI Card")
class Cash:
    def pay(self):
        print("Amount")
payments=[UPI(),Card(),Cash()]
for P in payments:
    P.pay()
    def Pay_now(obj):
        if isinstance(obj,UPI):
            obj.pay()
        elif isinstance(obj,Card):
            obj.pay()
        else:
            print("Invalid Payment")
Pay_now(UPI())
Pay_now(Card())
Pay_now(Cash())



