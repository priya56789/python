class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(f"The title of book is {self.title} and author is {self.author} and  the price is {self.price}")
def add_book():
    title=input()
    author=input()
    price=int(input())
    obj=Book(title,author,price)
    try:
        if price<0:
            raise ValueError("price cannot be negative")
        else:
            return obj
    except ValueError as ve:
        print(ve)
    finally:
            print(price)