import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')  
django.setup()


from django.core.files import File
from apps.main.models import Product
from django.contrib.auth.models import User


user = User.objects.create_user(username='UsuarioQuePopula', password='12345')

image_paths = [
    'static/assets/img/fotos/tenis1.jpg',
    'static/assets/img/fotos/tenis2.jpg',
    'static/assets/img/fotos/tenis3.jpg',
    'static/assets/img/fotos/tenis4.jpg',
    'static/assets/img/fotos/tenis5.jpg',
    'static/assets/img/fotos/tenis6.jpg',
    'static/assets/img/fotos/tenis7.jpg',
    'static/assets/img/fotos/tenis8.jpg',
    'static/assets/img/fotos/tenis9.jpg',
    'static/assets/img/fotos/tenis10.jpg',
    'static/assets/img/fotos/tenis11.jpg',
    'static/assets/img/fotos/tenis12.jpg',
]


for i, path in enumerate(image_paths):
    with open(path, 'rb') as image_file:
        product = Product(
            name=f'product {i+1}',
            description = f'Description for product {i+1}',
            price = 109.99 + i,
            user=user
        )
        product.image.save(f'tenis{i+1}.jpg', File(image_file), save=True)
        product.save()

print('Banco populadoooo')