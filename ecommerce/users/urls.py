from django.urls import path
from .views import login_vendor

urlpatterns = [
    path("login/", login_vendor, name="login"),
]
