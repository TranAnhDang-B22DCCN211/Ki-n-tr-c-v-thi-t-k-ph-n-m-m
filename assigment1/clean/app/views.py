from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render # <-- Đưa lên đầu cho chuẩn

# Import UseCases
from usecases.books import ListBooksUseCase, CreateBookUseCase
from usecases.cart import GetCartUseCase, AddToCartUseCase

# Import Infrastructure & Serializers
from infrastructure.repositories import DjangoBookRepository, DjangoCartRepository
from .serializers import CustomerSerializer, BookSerializer, CartSerializer

# --- PHẦN 1: AUTH ---
class RegisterView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login Success", "user": username})
        return Response({"error": "Invalid credentials"}, status=401)

# --- PHẦN 2: BOOKS ---
class BookListView(APIView):
    def get(self, request):
        repo = DjangoBookRepository()
        use_case = ListBooksUseCase(repo)
        books = use_case.execute()
        return Response(BookSerializer(books, many=True).data)

@method_decorator(csrf_exempt, name='dispatch')
class AddBookView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        price = request.data.get('price')
        stock = request.data.get('stock')

        repo = DjangoBookRepository()
        use_case = CreateBookUseCase(repo)

        try:
            book = use_case.execute(title, author, price, stock)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --- PHẦN 3: CART ---
class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        repo = DjangoCartRepository()
        use_case = GetCartUseCase(repo)
        cart = use_case.execute(request.user)
        return Response(CartSerializer(cart).data)

@method_decorator(csrf_exempt, name='dispatch')
class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book_id')
        quantity = int(request.data.get('quantity', 1))

        repo = DjangoCartRepository()
        use_case = AddToCartUseCase(repo)
        
        # Đúng: Phải truyền nguyên cục request.user (Object)
        success = use_case.execute(request.user, book_id, quantity) 
        if success:
            return Response({"message": "Added to cart clean!"})
        return Response({"error": "Book not found"}, status=404)

# --- PHẦN 4: GIAO DIỆN WEB (INDEX) ---
def index(request):
    return render(request, 'index.html')