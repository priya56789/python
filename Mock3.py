class Service:
    def m1(self):
        raise Exception("Method which handles errors")
    def m2(self):
        try:
            self.m1()
        except Exception as e:
            print(e)
        finally:
            print("Execution Completed")
obj=Service()
obj.m2()







