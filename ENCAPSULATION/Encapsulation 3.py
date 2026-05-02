# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)



class SecureFile:
    def __init__ (self,data):
        self.__data=data
        self.__log=[]
    def read(self,password):
        if password==1234:
            return self.__data
        else:
            self.__log.append("unauthorised attempt")
            return("some one access")
s=SecureFile(123456)
print(s.read(1234))
print(s.read(2178))