# Q6. Create a class Book with:
# instance attributes title, author
# a class variable total_books
# a class method from_string(cls, book_str) that creates an object from "title-author" format
# a static method is_valid_title(title) that checks if title has at least 3 characters
# increment total_books for every book created
# Demonstrate:
# Creating books using both the constructor and the class method
# Validating titles before creation



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











