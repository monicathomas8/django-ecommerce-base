from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem


def checkout(request):
    """
    Show checkout page and create an order from the cart on POST.
    """
    cart = Cart(request)

    if request.method == "POST":
        # If cart is empty, send them back
        if len(cart) == 0:
            return redirect("cart_detail")

        # Create the order (attach user if logged in)
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None
        )

        # Create order items from the cart
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                price=item["price"],
            )

        # Clear the cart
        cart.clear()

        # Redirect to a simple success page
        return redirect("order_success", order_id=order.id)

    # GET request: just show checkout with cart summary
    return render(request, "orders/checkout.html", {"cart": cart})


def order_success(request, order_id):
    """
    Simple order confirmation page.
    """
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order_success.html", {"order": order})
