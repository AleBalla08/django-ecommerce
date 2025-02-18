from django import forms
from .models import Product, Profile, User
from django.contrib.auth.forms import PasswordChangeForm

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

    profile_photo = forms.ImageField(required=False)

    def clean_register_name(self):
        name = self.cleaned_data.get("register_name")

        if name:
            name = name.strip()
            if " " not in name:
                return name
            else:
                raise forms.ValidationError('Not possible to put spaces in this field')
            
class UpdateProfile(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class':'form-control', 'readonly':'readonly'}
    ))

    register_name = forms.CharField(label='Name', required=True, max_length=20, widget=forms.TextInput(
        attrs={
            "class":"form-control",
        }
    ))

    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['profile_photo']

    def clean_register_name(self):
        name = self.cleaned_data.get("register_name").strip()
        if " " in name:
            raise forms.ValidationError("Not possible to put spaces in this field")
        return name
    

    
class UpdatePassword(PasswordChangeForm):
    old_password= forms.CharField(
        label="Current Password", required=True,
        widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Type your current password"})
    )

    new_password1 = forms.CharField(
        label="New Password", required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Type your new Password'})
    )

    new_password2 = forms.CharField(
        label="Confirm your password", required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm the new password'})
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


