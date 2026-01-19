

from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    # Dùng kế thừa AbstractUser là đủ yêu cầu (có sẵn username, pass, email)
    pass
