from django.contrib import admin
from django.urls import path
from core.views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/users/<int:user_id>/', UserDetailView.as_view()), # API nội bộ
]