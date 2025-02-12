from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'cart'  # Garante que podemos usar "cart:cart_view" nos templates

urlpatterns = [
    path('', cartView, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', update_item, name='update_item'),
    path('checkout/', checkout, name="checkout"),
] 