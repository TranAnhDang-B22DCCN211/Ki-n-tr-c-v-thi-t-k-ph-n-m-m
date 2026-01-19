from rest_framework import generics, status, views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import CustomerSerializer

# 1. API Đăng ký
class RegisterView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

# 2. API Đăng nhập
class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"message": "Đăng nhập thành công!", "user": username}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Sai tài khoản hoặc mật khẩu"}, status=status.HTTP_401_UNAUTHORIZED)

# 3. API Đăng xuất
class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Đăng xuất thành công!"}, status=status.HTTP_200_OK)