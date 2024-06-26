from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password", "username"]


