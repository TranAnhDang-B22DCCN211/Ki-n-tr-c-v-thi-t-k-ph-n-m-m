from django.contrib import admin
from django.urls import path
from core.views import CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL: /api/cart/<user_id>/
    path('api/cart/<int:user_id>/', CartView.as_view()),
]