from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer

# 1. Đăng ký
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 2. Đăng nhập (Trả về ID user để các service khác dùng)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login OK", "user_id": user.id, "username": user.username})
        return Response({"error": "Sai tài khoản/mật khẩu"}, status=401)

# 3. Lấy thông tin User (Internal API - Service khác sẽ gọi cái này)
class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            return Response({"id": user.id, "username": user.username})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)