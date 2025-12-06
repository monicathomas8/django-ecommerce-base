from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from catalogue.models import Product
from .cart import Cart


def cart_detail(request):
    """
    Display the contents of the cart.
    """
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})


@require_POST
def add_to_cart(request, product_id):
    """
    Add a product to the cart or update its quantity.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get("quantity", 1))
    cart.add(product=product, quantity=quantity)

    return redirect("cart_detail")


def remove_from_cart(request, product_id):
    """
    Remove a product from the cart.
    """
    cart = request.session.get("cart", {})
    product_key = str(product_id)
    if product_key in cart:
        del cart[product_key]
        request.session["cart"] = cart       # Update the session cart

    return redirect("cart_detail")
