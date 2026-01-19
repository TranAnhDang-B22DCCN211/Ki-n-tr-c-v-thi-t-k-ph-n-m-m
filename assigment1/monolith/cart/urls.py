# cart/urls.py
from django.urls import path
from .views import CartView, AddToCartView

urlpatterns = [
    path('api/cart/', CartView.as_view(), name='view-cart'),
    path('api/cart/add/', AddToCartView.as_view(), name='add-to-cart'),
]