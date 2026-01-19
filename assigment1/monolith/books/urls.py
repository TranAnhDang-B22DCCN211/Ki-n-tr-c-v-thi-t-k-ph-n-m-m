
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('api/books/', BookListView.as_view(), name='book-list'),
]
from .views import BookListView, index # <-- Import hàm index

urlpatterns = [
    path('', index, name='home'), # <-- Thêm dòng này để vào trang chủ
    path('api/books/', BookListView.as_view(), name='book-list'),
]