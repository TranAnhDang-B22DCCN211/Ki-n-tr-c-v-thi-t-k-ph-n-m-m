from domain.repositories import BookRepositoryInterface, CartRepositoryInterface
from app.models import Book, Cart, CartItem, Customer # <-- Import thêm Customer

# --- REPO CHO SÁCH ---
class DjangoBookRepository(BookRepositoryInterface):
    def get_all_books(self):
        return Book.objects.all()

    def create_book(self, title, author, price, stock):
        return Book.objects.create(
            title=title, 
            author=author, 
            price=price, 
            stock=stock
        )

# --- REPO CHO GIỎ HÀNG (Đã sửa lỗi LazyObject) ---
class DjangoCartRepository(CartRepositoryInterface):
    
    # Hàm hỗ trợ: Biến mọi loại user (Lazy, String, Object) thành Customer thật
    def _get_real_customer(self, user):
        if hasattr(user, 'id') and user.id:
            # Nếu là Object (có ID), lấy lại từ DB cho chắc chắn
            return Customer.objects.get(id=user.id)
        elif isinstance(user, str):
            # Nếu là String (tên đăng nhập), tìm theo username
            return Customer.objects.get(username=user)
        else:
            raise ValueError("User invalid")

    def get_cart(self, user):
        # Ép kiểu user trước khi query
        customer = self._get_real_customer(user)
        cart, _ = Cart.objects.get_or_create(customer=customer)
        return cart

    def add_to_cart(self, user, book_id, quantity):
        # --- BỎ TRY/EXCEPT ĐỂ DEBUG ---
        # try:
        
        # 1. Ép kiểu User
        customer = self._get_real_customer(user)
        
        # 2. In ra kiểm tra xem nó lấy được ai (Nhìn vào Terminal để xem)
        print(f"DEBUG: Customer found: {customer}") 
        print(f"DEBUG: Book ID requested: {book_id}")

        # 3. Lấy giỏ hàng
        cart, _ = Cart.objects.get_or_create(customer=customer)
        
        # 4. Lấy sách (Nghi ngờ lỗi ở đây hoặc ở trên)
        book = Book.objects.get(id=book_id)
        
        # 5. Thêm vào
        item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
        return True
            
        # except (Book.DoesNotExist, Customer.DoesNotExist):
        #     print("DEBUG: Lỗi không tìm thấy Book hoặc Customer!")
        #     return False