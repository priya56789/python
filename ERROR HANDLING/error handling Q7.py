# Create a class UserInput with a method get_integer(value). Handle ValueError
# and TypeError using separate except blocks.


class UserInput:
    def get_integer(self,value):
        try:
            number=int(value)
            return value
        except ValueError as ve:
            print("ValueError:The value is not converted into integer")
        except TypeError as te:
            print("TypeError:Invalid type for conversion")
obj=UserInput()
print(obj.get_integer("25"))
obj.get_integer("bhavana")
obj.get_integer(None)