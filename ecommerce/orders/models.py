from django.conf import settings
from django.db import models

class Order(models.Model):

    STATUS = [
        ('pending', 'Pendente'),
        ('processing', 'Precessando'),
        ('shipped', 'Enviado'),
        ('delivered', 'Enviado')
    ]

    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'

    )

    product = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.customer}"