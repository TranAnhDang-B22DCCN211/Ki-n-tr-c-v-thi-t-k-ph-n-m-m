# cart/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from books.serializers import BookSerializer # Dùng lại cái cũ cho tiện

class CartItemSerializer(serializers.ModelSerializer):
    # Khi xem giỏ hàng sẽ hiện full thông tin sách (Title, Price...)
    book = BookSerializer(read_only=True) 
    book_id = serializers.IntegerField(write_only=True) 
    class Meta:
        model = CartItem
        fields = ['id', 'book', 'book_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'created_at', 'items']