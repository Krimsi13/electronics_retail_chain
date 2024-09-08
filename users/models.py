from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", **NULLABLE)
    city = models.CharField(max_length=25, verbose_name="Город", **NULLABLE)
    enterprise = models.CharField(max_length=100, verbose_name="Предприятие", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
