from abc import ABC, abstractmethod

# 1. Interface cho SÁCH (Có create_book)
class BookRepositoryInterface(ABC):
    @abstractmethod
    def get_all_books(self):
        pass
    
    @abstractmethod
    def create_book(self, title, author, price, stock):
        pass

# 2. Interface cho GIỎ HÀNG (KHÔNG ĐƯỢC CÓ create_book ở đây)
class CartRepositoryInterface(ABC):
    @abstractmethod
    def get_cart(self, user):
        pass

    @abstractmethod
    def add_to_cart(self, user, book_id, quantity):
        pass