from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude= ['user',]
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

class LoginForm(forms.Form):
    
    name_login=forms.CharField(label='login Name', required=True, max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Ex: Jack123",
        }
    ))

    password = forms.CharField(label='Password', required=True, max_length=50, widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Type your Password"
        }
    ))


class RegisterForm(forms.Form):

    register_name = forms.CharField(label='Name', required=True, max_length=20, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Ex: Jack123"
        }
    ))

    email = forms.EmailField(label="Email", required=True, max_length=50, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"exemple123@expl.com"
        }
    ) )

    pass1 = forms.CharField(label="Password", required=True, max_length=20, widget= forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Type your password"
        }
    ))

    pass2 = forms.CharField(label="Confirm your Password", required=True, max_length=20, widget= forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Type your password"
        }
    ))

    def clean_register_name(self):
        name = self.cleaned_data.get("register_name")

        if name:
            name = name.strip()
            if " " not in name:
                return name
            else:
                raise forms.ValidationError('Not possible to put spaces in this field')
