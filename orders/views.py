from django.shortcuts import render


def checkout(request):
    """
    Basic checkout placeholder view.
    This can be updates to collect
    shipping details and create an order.
    """
    return render(request, "orders/checkout.html")
