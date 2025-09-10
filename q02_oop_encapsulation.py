# src/q02_oop_encapsulation.py
class Book:
    def __init__(self, title: str, author: str, price: float, discount: float = 0.1):
        self.title = title
        self.author = author
        self.price = float(price)
        self._discount = 0.0
        self.discount = discount  # use setter to validate

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float) -> None:
        try:
            v = float(value)
        except (TypeError, ValueError):
            raise ValueError("Discount must be a number between 0.0 and 0.9")
        if not (0.0 <= v <= 0.9):
            raise ValueError("Discount must be between 0.0 and 0.9")
        self._discount = v

    def get_price_after_discount(self) -> float:
        return self.price * (1 - self._discount)

    def __str__(self):
        return f"{self.title} by {self.author} - Price: {self.price} (discount: {self._discount})"

if __name__ == "__main__":
    b = Book("Clean Architecture", "Robert C. Martin", 699.0)
    print("Original price:", b.price)
    print("Default discount:", b.discount)
    b.discount = 0.2
    print("After setting discount to 0.2 ->", b.get_price_after_discount())

    # demonstrate validation (commented out to avoid raising on normal run)
    # b.discount = 1.0  # would raise ValueError
