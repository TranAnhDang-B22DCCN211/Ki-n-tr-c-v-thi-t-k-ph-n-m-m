from django.db import models

class Cart(models.Model):
    user_id = models.IntegerField() # Lưu ID user từ Auth Service
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book_id = models.IntegerField() # Lưu ID sách từ Book Service
    quantity = models.IntegerField(default=1)
    
    # Lưu giá lúc mua để lỡ Book Service đổi giá cũng ko ảnh hưởng
    price = models.DecimalField(max_digits=10, decimal_places=2)