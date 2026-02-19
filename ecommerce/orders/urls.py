from django.urls import path
from . import views
from .views import orders_list, order_create

urlpatterns = [
    path("", views.orders_list, name="orders_list"),
    path("novo/", views.order_create, name="order_create"),
    path("", orders_list, name="orders_list"),
    path("create/", order_create, name="order_create"),

]
