# Use Case nhận vào một cái Repository bất kỳ (miễn là tuân thủ Interface)
class ListBooksUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        # Logic nghiệp vụ ở đây (nếu có)
        return self.repository.get_all_books()
    # clean/usecases/books.py

# Class cũ giữ nguyên
class ListBooksUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all_books()

# THÊM CLASS MỚI NÀY:
class CreateBookUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, title, author, price, stock):
        # Ở đây có thể thêm logic kiểm tra (ví dụ: giá không được âm)
        if float(price) < 0:
            raise ValueError("Price cannot be negative")
            
        return self.repository.create_book(title, author, price, stock)