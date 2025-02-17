from django.contrib import admin
from .models import CartItem, Order, UserAddress, OrderItem

admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(UserAddress)
admin.site.register(OrderItem)

# Register your models here.
