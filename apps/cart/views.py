from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from apps.main.models import Product

# Create your views here.

def cartView(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart-temp/cart.html', {'cart_items': cart_items, 'total': total})



def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_view')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:cart_view')

def update_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    new_quantity = int(request.POST.get('quantity'))

    if new_quantity > 0:
        cart_item.quantity = new_quantity
        cart_item.save()

    return redirect('cart:cart_view')