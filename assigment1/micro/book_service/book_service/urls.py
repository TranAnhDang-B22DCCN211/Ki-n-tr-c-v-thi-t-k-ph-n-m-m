from django.contrib import admin
from django.urls import path
from core.views import BookListCreateView, BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListCreateView.as_view()),
    path('api/books/<int:pk>/', BookDetailView.as_view()),
]