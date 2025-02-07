
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Product

def custom_login_required(view_func):
    def wrapper(request, *arg, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'You need to be loged to proceed')
            return redirect('login')
        return view_func(request, *arg, **kwargs)
    return wrapper


    

def store(request):
    context = {'products': Product.objects.all()}
    return render(request, 'store/store.html', context)






def newProduct(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not authenticated, Log-in first')
        return redirect('login')
    
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            product.save()
            messages.success(request, 'Product Posted')
            return redirect('store')
        else:
            print(form.errors)

    return render(request, 'store/new_product.html', {'form': form})




def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            password = form['password'].value()
            user = auth.authenticate(
                request,
                username = name,
                password = password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'User Loged in')

                return redirect('store')
            else:
                messages.error(request, 'error at trying to Login')
                return redirect('login') 
    return render(request, 'store/login.html', {'form':form})


def register(request):
    form = RegisterForm()

    def clean_register_name(self):
        name = self.cleaned_data.get("register_name")

        if name:
            if " " not in name:
                return name
            else:
                messages.error(request, "You can't put blank spaces in the name field")
                return redirect('register')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form['pass1'].value() != form['pass2'].value():
                messages.error(request, "The passwords aren't equal")
                return redirect('register')
            name = form['register_name'].value()
            email = form['email'].value()
            password = form['pass1'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Username already in use')
                return redirect('register')

            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()
            messages.success(request, 'User created succesfully')
            return redirect('login')
        
    return render(request, 'store/register.html', {'form':form})
    
def logoutView(request):
    auth.logout(request)
    messages.success(request, 'User Logouted succesfully')
    return redirect('login')



