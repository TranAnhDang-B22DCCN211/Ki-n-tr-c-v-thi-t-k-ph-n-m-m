
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('accounts.urls')),
    path('', include('cart.urls')), 
]