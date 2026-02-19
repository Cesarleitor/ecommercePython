from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Order(models.Model):
    COLOR_CHOICES = [
        ("black", "Preto"),
        ("white", "Branco"),
        ("red", "Vermelho"),
        ("blue", "Azul"),
        ("green", "Verde"),
    ]

    SIZE_CHOICES = [
        ("pp", "PP"),
        ("p", "P"),
        ("m", "M"),
        ("g", "G"),
        ("gg", "GG"),
    ]

    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=120)
    customer = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="black")
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, default="m")

    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.product} - {self.customer}"