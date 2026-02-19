from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def orders_list(request):
    user = request.user

    if user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(vendor=user)

    return render(request, "orders/list.html", {"orders": orders})


@login_required
def order_create(request):
    if request.method == "POST":
        product = request.POST.get("product")
        customer = request.POST.get("customer")
        quantity = request.POST.get("quantity")

        Order.objects.create(
            vendor=request.user,
            product=product,
            customer=customer,
            quantity=quantity,
        )
        return redirect("orders_list")

    return render(request, "orders/create.html")
