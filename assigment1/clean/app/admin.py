from django.contrib import admin
from .models import Customer, Book, Cart, CartItem

# Đăng ký các bảng để quản lý

admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(CartItem)