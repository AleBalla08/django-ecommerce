from django.contrib import admin
from .models import CartItem, Order, UserAddress

admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(UserAddress)

# Register your models here.
