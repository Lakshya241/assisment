# src/q03_oop_inheritance.py
class Book:
    def __init__(self, title: str, author: str, price: float, discount: float = 0.0):
        self.title = title
        self.author = author
        self.price = float(price)
        self._discount = float(discount)

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

    def get_price_after_discount(self) -> float:
        return self.price * (1 - self._discount)

class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size: float, discount: float = 0.0):
        super().__init__(title, author, price, discount)
        self.file_size = float(file_size)

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base}, File Size: {self.file_size}MB"

if __name__ == "__main__":
    eb = EBook("Python Tricks", "Dan Bader", 299.0, file_size=2.5, discount=0.15)
    print(eb.get_details())
    print("Discounted price:", eb.get_price_after_discount())
