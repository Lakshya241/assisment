# src/q04_oop_polymorphism.py
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = float(price)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size: float):
        super().__init__(title, author, price)
        self.file_size = float(file_size)

    def get_details(self) -> str:
        return f"{super().get_details()}, File Size: {self.file_size}MB"

def print_details(obj):
    # duck-typed: call get_details if present
    if hasattr(obj, "get_details") and callable(getattr(obj, "get_details")):
        print(obj.get_details())
    else:
        print(repr(obj))

if __name__ == "__main__":
    items = [
        Book("Deep Work", "Cal Newport", 399.0),
        EBook("Automate the Boring Stuff", "Al Sweigart", 199.0, 3.2),
        Book("The Mythical Man-Month", "Frederick P. Brooks Jr.", 299.0),
    ]

    for it in items:
        print_details(it)
