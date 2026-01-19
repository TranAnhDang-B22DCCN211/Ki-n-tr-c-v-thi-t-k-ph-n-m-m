# UseCase: Lấy giỏ hàng
class GetCartUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        return self.repository.get_cart(user)

# UseCase: Thêm vào giỏ
class AddToCartUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, book_id, quantity):
        return self.repository.add_to_cart(user, book_id, quantity)