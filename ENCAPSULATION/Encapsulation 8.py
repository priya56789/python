# 8. Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal
# list)

class ShoppingCart:
    def __init__(self):
        self.__item=[]
    def add(self,item):
        self.__item.append(item)
    def remove(self,item):
        self.__item.remove(item)
    def get_item(self):
        return self.__item.copy()
cart=ShoppingCart()
cart.add("Banana")
cart.add("Sapota")
print(cart.get_item())
cart.remove("Sapota")
print(cart.get_item())
x=cart.get_item()
x.append("Apple")
