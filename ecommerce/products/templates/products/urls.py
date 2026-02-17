from django.urls import path

from ecommerce.products.views import product_list

urlpatterns = [
    path('', product_list, name ='product_list')

    ]
