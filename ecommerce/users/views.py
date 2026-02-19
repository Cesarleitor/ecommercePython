from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_vendor(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("LOGIN:", username, password)  # DEBUG

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print("OK LOGIN")
            return redirect("/orders/")
        else:
            print("ERRO LOGIN")
            messages.error(request, "Usuário ou senha inválidos")

    return render(request, "users/login.html")


def login_vendor(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # 👇 lógica admin x vendedor
            if user.is_superuser:
                return redirect("orders_list")

            if user.is_vendor:
                return redirect("order_create")

            return redirect("orders_list")

        messages.error(request, "Usuário ou senha inválidos")

    return render(request, "users/login.html")

