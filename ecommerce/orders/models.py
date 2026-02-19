from django.conf import settings
from django.db import models

class Order(models.Model):
    STATUS = [
        ('pending', 'Pendente'),
        ('processing', 'Processando'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregue'),
    ]

    COLOR_CHOICES = [
        ("preto", "Preto"),
        ("branco", "Branco"),
        ("vermelho", "Vermelho"),
        ("azul", "Azul"),


    ]

    SIZE_CHOICES = [
        ("pp", "PP"),
        ("p", "P"),
        ("m", "M"),
        ("g", "G"),
        ("gg", "GG"),
    ]

    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    product = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    quantity = models.IntegerField()

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="preto")
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, default="m")

    status = models.CharField(max_length=20, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.customer}"