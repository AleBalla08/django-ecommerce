from django import forms
from .models import *

class AddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        exclude = ['user']
        labels = {
            'address':'Address',
            'neighborhood':'Neighborhood',
            'city':'City',
            'state':'State',
            'country':'Country'
        }

        widgets = {
            'address':forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Ex: 12th street, 123'}),
            'neighborhood':forms.TextInput(attrs={'class' : 'form-control'}),
            'city':forms.TextInput(attrs={'class' : 'form-control'}),
            'state':forms.TextInput(attrs={'class' : 'form-control'}),
            'country':forms.TextInput(attrs={'class' : 'form-control'})
        }