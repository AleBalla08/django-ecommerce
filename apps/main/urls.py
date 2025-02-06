from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name='store'),
    path('checkout/', checkout, name="checkout"),
    path('new-product/', newProduct, name='new-product'),
    path('login/', login, name="login"),
    path('register/', register, name='register'),
    path('logout/', logoutView, name='logout'),
]