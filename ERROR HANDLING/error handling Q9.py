# Create a class Service with a method that calls another method which raises an
# exception. Catch and handle the exception in the Service class.


class Service:
    def m1(self):
        raise Exception("Method which handles errors")
    def m2(self):
        try:
            self.m1()
        except Exception as e:
            print(e)
obj=Service()
obj.m2()