from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_vendor(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Admin vai para o painel do Django Admin
            if user.is_superuser:
                return redirect("/admin/")

            # Vendedor vai para criar pedido
            if user.is_vendor:
                return redirect("order_create")

            # Qualquer outro usuário vai para lista
            return redirect("orders_list")

        messages.error(request, "Usuário ou senha inválidos")

    return render(request, "users/login.html")
