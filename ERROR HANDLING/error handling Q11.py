#  Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class.


class  LoginSystem:
    def login(self,password):
        self.password=password
        try:
            if self.password!="12345":
                raise Exception("Invalid Password")
            print("Validation Successful")
        except Exception as e:
            print(e)
        finally:
            print("Completed Execution")
p=LoginSystem()
p.login("123456")




