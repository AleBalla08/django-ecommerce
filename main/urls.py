from django.urls import path
from main.views import *

urlpatterns = [
    path('', store, name='store'),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout")
]