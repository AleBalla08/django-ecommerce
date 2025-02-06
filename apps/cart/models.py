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
