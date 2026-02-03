from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        
        cart, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={"quantity": 1},
        )
        if not created:
            cart.quantity += 1
            cart.save()
    else:
        Cart.objects.create(user=None, product=product, quantity=1)

    return redirect(request.META.get("HTTP_REFERER", "/"))


def cart_change(request, product_slug):
    ...


def cart_remove(request, product_slug):
    ...
