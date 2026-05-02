# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price()


class Product:
    def __init__(self,price,discount):
        self.__price=price
        self.__discount=discount
    def get_final_price(self):
        if self.__price<0:
            return "Invalid price"
        if self.__discount>70:
            return "Invalid discount"
        return self.__price*(1-self.__discount/100)
p1=Product(1000,200)
p2=Product(-2000,400)
print( p1.get_final_price())
print(p2.get_final_price())
