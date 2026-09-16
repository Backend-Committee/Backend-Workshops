from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    
    def __str__(self):
        return self.username