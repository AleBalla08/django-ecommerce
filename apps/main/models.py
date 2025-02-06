from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default='Image')
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=False, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False, null=False, default=None)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return f'Product [name = {self.name}]'
    
