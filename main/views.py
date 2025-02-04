from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import *

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def newProduct(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Posted')
            return redirect('store')
    # if not request.user.is_authenticated:
    #     messages.error(request, 'User dont authenticated, Log-in first')
    #     return redirect('login')

    return render(request, 'store/new_product.html', {'form':form})