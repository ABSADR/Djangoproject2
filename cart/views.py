from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

from cart.models import Cart, CartItem
from product.models import Product


def add_to_cart(request, product_id):
    print(f'user:{request.user}')
    print(f'product id:{product_id}')
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    print(f'cart created {created}')
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    print(f'cartitem created {cart_item}')
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    products = Product.objects.all()
    user_id = request.user.id
    cart = None

    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    cart_items = cart.items.all()
    print(f'cart items {cart_items}')
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    # total_price = cart.items.aggregate(Sum('product__price'))['product__price__sum'] or 0
    # total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
