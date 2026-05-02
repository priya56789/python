# • Create a class Transaction with a method process() that uses try, except, and
# finally blocks to ensure a cleanup message is always printed.


class Transaction:
    def process(self,balance,amount):
        self.balance=balance
        try:
            if amount>self.balance:
                raise Exception("Balance insufficient")
            print("Transaction completed")
        except Exception as e:
            print(e)
        finally:
            print("Execution completed by priyanka")
obj=Transaction()
obj.process(200,500)