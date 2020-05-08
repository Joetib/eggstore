from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username or self.email