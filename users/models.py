from django.contrib.auth.models import AbstractUser
from django.db import models
from spa_app.models import NULLABLE


class User(AbstractUser):
    """Model of users"""
    username = None

    email = models.EmailField(unique=True, max_length=50, verbose_name='email')
    tg_name = models.CharField(unique=True, max_length=50, verbose_name='telegram_username')
    chat_id = models.CharField(verbose_name='chat_id', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
