# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

Customer = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Hàm này để tạo user và tự động mã hóa password
        user = Customer.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user