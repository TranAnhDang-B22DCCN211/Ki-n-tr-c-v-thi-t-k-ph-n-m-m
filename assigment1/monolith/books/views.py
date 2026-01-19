# books/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from .views import BookListView, index # <-- Import hàm index

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')