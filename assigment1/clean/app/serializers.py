from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book, Cart, CartItem

Customer = get_user_model()

# 1. Serializer cho User (Đăng ký)
class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = Customer.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# 2. Serializer cho Sách (Đã có)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# 3. Serializer cho Giỏ hàng
class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items']