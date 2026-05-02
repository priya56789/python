# Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.


class PasswordValidator(Exception):
    def validate(self,password):
        if len(password)<8:
            raise Exception("password is not valid")
        else:
            print("valid")
obj=PasswordValidator()
try:
    obj.validate("2178636890")
    obj.validate("2178217")
except Exception as e:
    print(e)
finally:
    print("Execution done")