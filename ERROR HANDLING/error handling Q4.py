#  Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18.


class InvalidAgeError(Exception):
    pass
class Voter:
    def check_eligibility(self,age):
        if age<18:
            raise InvalidAgeError("age is not valid")
        else:
            print("Valid age")
obj=Voter()
try:
    obj.check_eligibility(15)
except InvalidAgeError as e:
    print(e)
finally:
    print("Sasi is going to marry")

