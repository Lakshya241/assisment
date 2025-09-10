# src/q05_oop_all_in_one.py
from typing import List

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        try:
            self.value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Price value must be a number")
        if self.value < 0:
            raise ValueError("Price cannot be negative")
        self.currency = str(currency)

    def __repr__(self) -> str:
        return f"{self.currency} {self.value:.2f}"

    __str__ = __repr__

class Book:
    def __init__(self, title: str, author: str, price: Price):
        self.title = str(title)
        self.author = str(author)
        if not isinstance(price, Price):
            raise TypeError("price must be a Price instance")
        self.price = price

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price})"

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} - {self.price}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author) == (other.title, other.author)

    @classmethod
    def from_dict(cls, d: dict):
        title = d.get("title")
        author = d.get("author")
        price_raw = d.get("price")
        currency = d.get("currency", "INR")
        if isinstance(price_raw, Price):
            price = price_raw
        else:
            price = Price(price_raw, currency)
        return cls(title, author, price)

class Inventory:
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def remove_book(self, title: str, author: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title == title and b.author == author:
                del self._books[i]
                return True
        return False

    def find_by_author(self, author: str):
        return [b for b in self._books if b.author == author]

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __repr__(self):
        return f"Inventory({len(self)} books)"

if __name__ == "__main__":
    data = [
        {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "price": 399.0},
        {"title": "Clean Code", "author": "Robert C. Martin", "price": 499.0},
        {"title": "Refactoring", "author": "Martin Fowler", "price": 599.0},
    ]

    inv = Inventory()
    for d in data:
        b = Book.from_dict(d)
        inv.add_book(b)

    print("All books in inventory:")
    for b in inv:
        print(" -", b)

    removed = inv.remove_book("Clean Code", "Robert C. Martin")
    print("\nRemoved Clean Code:", removed)
    print("Inventory length:", len(inv))

    print("\nBooks by Martin Fowler:")
    for b in inv.find_by_author("Martin Fowler"):
        print(" -", b)
