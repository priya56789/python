class Employee:
    bonus_rate=0.1
    def __init__ (self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
         return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_bonus):
        cls.bonus_rate=new_bonus
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return True
        return False
Emp1=Employee("Priyanka",10000)
Emp2=Employee("Ankitha",20000)
print(Emp1.final_salary())
print(Emp2.final_salary())
Employee.update_bonus(0.5)
print(Employee.bonus_rate)
print(Emp1.final_salary())
print(Emp2.final_salary())
print(Employee.is_valid_salary(20000))



class Product:
    base_tax_rate=500
    def __init__ (self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        final_price=self.base_price+Product.base_tax_rate
        return final_price
    @classmethod
    def change_tax_rate(cls,new):
        cls.base_tax_rate=new
    @staticmethod
    def is_valid(price):
        if price>0:
            return True
        return False
P1=Product("Fridge",35000)
P2=Product("TV",40000)
Product.change_tax_rate(1000)
print(Product.base_tax_rate)
print(P1.final_price())
print(P2.final_price())
print(Product.is_valid(20000))


class Book:
    total_books=0
    def __init__ (self,title,author):
        if Book.is_valid_title(title):
            self.title=title
            self.author=author
            Book.total_books+=1
        else:
            return None
    @classmethod
    def from_string(cls,Book_str):
        cls.Book_str=Book_str.split("_")
        book3=Book("Python","Priyanka")
        return book3
    @staticmethod
    def is_valid_title(title):
        if len(title)>3:
            return True
        return False
print(Book.is_valid_title("Python"))
print(Book.is_valid_title("Go"))
Book1=Book("Python","Gudia")
Book2=Book("Title","Author")
print(Book1.from_string("title"))
print(Book.total_books)



















