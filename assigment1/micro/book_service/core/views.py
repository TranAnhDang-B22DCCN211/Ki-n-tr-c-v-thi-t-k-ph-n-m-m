from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Xem danh sách & Thêm sách
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Xem chi tiết, Sửa, Xóa một cuốn (Service Cart sẽ cần gọi cái này để check giá)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer