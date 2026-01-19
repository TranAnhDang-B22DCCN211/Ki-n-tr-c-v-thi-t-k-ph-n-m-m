from django.urls import path
# THÊM 'index' VÀO CUỐI DÒNG IMPORT:
from .views import RegisterView, LoginView, BookListView, CartView, AddToCartView, AddBookView, index

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/books/', BookListView.as_view()),
    path('api/cart/', CartView.as_view()),
    path('api/cart/add/', AddToCartView.as_view()),
    path('api/books/add/', AddBookView.as_view()),
    
    path('', index, name='home'), # <-- Giờ nó mới hiểu 'index' là gì
]