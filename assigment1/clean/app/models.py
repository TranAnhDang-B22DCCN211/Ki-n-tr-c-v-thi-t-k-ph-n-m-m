from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# 1. CUSTOMER (User)
class Customer(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customer_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_user_permissions',
        blank=True
    )

# 2. BOOK (Sách) - Quan trọng: Phải có các dòng này form mới hiện
class Book(models.Model):
    title = models.CharField(max_length=255)       # Tên sách
    author = models.CharField(max_length=255)      # Tác giả
    price = models.DecimalField(max_digits=10, decimal_places=2) # Giá
    stock = models.IntegerField(default=0)         # Số lượng kho

    def __str__(self):
        return self.title

# 3. CART (Giỏ hàng)
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# 4. CART ITEM (Sách trong giỏ)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)