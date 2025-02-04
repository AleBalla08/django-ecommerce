from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  
        labels = {
            'name':'Name',
            'description':'Description',
            'image':'Image',
            'price':'Price'
                
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describe your product in details...'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ex: $9.99'})
        }