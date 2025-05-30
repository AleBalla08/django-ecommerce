from decimal import Decimal
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

from apps.cart.forms import AddressForm
from .models import *
from apps.main.models import Product
from django.contrib.auth.decorators import login_required  # Para views baseadas em função (FBV)
from apps.main.views import custom_login_required


# Create your views here.

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


@custom_login_required
def cartView(request):
    """Apenas exibe os itens no carrinho, sem criar pedidos"""
    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price() or 0 for item in cart_items)

    return render(request, 'cart-temp/cart.html', {'cart_items': cart_items, 'total': total})


@custom_login_required
def add_to_cart(request, product_id):
    """Adiciona um produto ao carrinho"""
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_view')


@custom_login_required
def remove_from_cart(request, item_id):
    """Remove um item do carrinho"""
    cart_item = CartItem.objects.filter(id=item_id, user=request.user).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart:cart_view')


@custom_login_required
def update_item(request, item_id):
    """Atualiza a quantidade de um item no carrinho"""
    cart_item = CartItem.objects.filter(id=item_id, user=request.user).first()
    if cart_item:
        new_quantity = int(request.POST.get('quantity'))
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect('cart:cart_view')


@custom_login_required
def checkout(request):
    """Cria um pedido apenas quando o usuário finaliza a compra"""
    cart_items = CartItem.objects.filter(user=request.user)
    print(cart_items)

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    form = AddressForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        address = form.save(commit=False)
        addressExists = UserAddress.objects.filter(
            user = request.user,
            address = address.address,
            neighborhood = address.neighnorhood,
            city = address.city,
            state = address.state,
            country = address.country
        ).exists()

        if not addressExists:
            address.user = request.user
            address.save()
        else:
            address = UserAddress.objects.filter(
                user = request.user,
                address = address.address,
                neighborhood = address.neighnorhood,
                city = address.city,
                state = address.state,
                country = address.country
            )

        delivery_method=request.POST.get("selected_delivery")
        payment_method=request.POST.get("selected_payment")

        if delivery_method == 'Normal':
            total_price += Decimal('6.00')
        elif delivery_method == 'Fast':
            total_price += Decimal('11.00')
        elif delivery_method == 'Ultra':
            total_price += Decimal('18.00')
            
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_price=total_price,
            payment_method=payment_method,
            delivery_method=delivery_method
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,

            )

        cart_items.delete()  

        messages.success(request, "Order successful!")
        return redirect("store")

    context = {
        "cart_items": cart_items,
        "total": total_price,
        "form": form,
    }

    return render(request, "cart-temp/checkout.html", context)




