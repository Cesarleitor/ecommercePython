from django.contrib import admin
from .models import Order

admin.site.index_title = 'Seja Bem-Vindo ao Gerenciamento de Rastreio'
admin.site.site_header = 'Sistema de Rastreio'
admin.site.site_title = 'Admin Rastreio'

admin.site.register(Order)
