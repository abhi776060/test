class Book:
    def __init__(self,price):
        self.price=price
    def __add__(self, other):
        return self.price + other.price
    def __lt__(self, other):
        return self.price < other.price


book1=Book(5)
book2=Book(9)
print(book1 + book2)
print(book1 < book2)