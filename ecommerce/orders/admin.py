from django.contrib import admin
from .models import Order

admin.site.index_title = 'Seja Bem-Vindo ao Gerenciamento de Pedidos'
admin.site.site_header = 'Sistema de Pedidos'
admin.site.site_title = 'Admin Pedidos'

admin.site.register(Order)
