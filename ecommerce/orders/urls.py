from django.urls import path
from . import views

urlpatterns = [
    path("", views.orders_list, name="orders_list"),
    path("create/", views.order_create, name="order_create"),
]