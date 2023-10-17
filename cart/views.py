from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.shortcuts import render, redirect

from cart.models import Cart, CartItem
from product.models import Product
from django.http import JsonResponse


@login_required()
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
    return redirect(request.META.get('HTTP_REFERER')) #Using this redirect to keep the user on the current page



@login_required
def cart_detail(request):
    '''
    I attempt to get a Cart instance associated with the logged-in user.
    I use [0] to access the first element of the tuple returned by get_or_create,
    which should be the Cart instance itself.
    '''
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = cart.cart_items.all()

    # Calculate the total price by summing the quantity * price for each item
    total_price = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0

    return render(request, 'cart/cart_detail.html',
                  {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')

def update_cart_item_quantity(request):
    def update_cart_item_quantity(request):
        if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            cart_item_id = request.POST.get("cart_item_id")
            new_quantity = int(request.POST.get("new_quantity"))

            # Perform the update in the database
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.quantity = new_quantity
            cart_item.save()

            # Calculate the new total price for the cart item
            new_total = cart_item.product.price * new_quantity

            # Recalculate the total price for the entire cart
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.cart_items.all()
            new_cart_total = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0

            return JsonResponse({"new_total": new_total, "new_cart_total": new_cart_total})

        return JsonResponse({"error": "Invalid request."})