# Q2. Design a class Product that:
# Maintains a base tax rate applicable to all products.
# Each product has a name and base price.
# Has a method to compute final price including tax.
# Can change tax rate for all products using one method.
# Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# Creating multiple products.
# Changing the tax rate.
# Showing updated prices and validity checks.






class Product:
    tax_rate = 0.1

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        print(self.name)
        print(self.base_price)

    def final_price(self):
        self.base_price += self.base_price + Product.tax_rate

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def is_validate(price):
        if price >= 0 and price <= 100000:
            return True
        else:
            return False


product1 = Product("Fridge", 45000)
product2 = Product("Cooler", 35000)
Product.change_tax_rate(0.8)
print(Product.tax_rate)
print(Product.is_validate(36000))
print(Product.is_validate(-10))