# src/q01_oop_book_basics.py
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

if __name__ == "__main__":
    b1 = Book("The Pragmatic Programmer", "Andrew Hunt", 399.0)
    b2 = Book("Clean Code", "Robert C. Martin", 499.0)
    b3 = Book("Introduction to Algorithms", "Cormen et al.", 1299.0)

    print(b1.get_details())
    print(b2.get_details())
    print(b3.get_details())
