from django.db import models
from apps.main.models import Product
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="cart_item"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class UserAdress(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_address"
    )
    address = models.CharField(max_length=50, blank=False, null=False)
    neighborhood = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return f'{self.address}'




class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="orders" 
    ) 
    cart_items = models.ManyToManyField(CartItem)  
    address = models.ForeignKey(UserAdress, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Pedido {self.id} de {self.user.username}"





