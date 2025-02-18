
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Product, Profile
from apps.cart.models import *
from django.contrib.auth import update_session_auth_hash

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





@custom_login_required
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
            profile_photo = form.cleaned_data.get("profile_photo")

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Username already in use')
                return redirect('register')

            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user_profile = Profile(user=user, profile_photo=profile_photo)
            user_profile.save()
            user.save()
            
            messages.success(request, 'User created succesfully')
            return redirect('login')
        
    return render(request, 'store/register.html', {'form':form})

@custom_login_required  
def logoutView(request):
    auth.logout(request)
    messages.success(request, 'User Logouted succesfully')
    return redirect('login')

@custom_login_required
def profileView(request):
    user = request.user
    userProfile = Profile.objects.filter(user=user).first()
    userOrders = Order.objects.filter(user=user) 
    orderItems = OrderItem.objects.filter(order__in=userOrders)  

    form = UpdateProfile(instance=userProfile, initial={'register_name':user.username, 'user_email':user.email})

    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=userProfile)

        if form.is_valid():
            user.username = form.cleaned_data['register_name']
            user.save()
            form.save()

            messages.success(request, 'Profile updated succesfully')
            return redirect('profile')

    context = {
        'userProfile': userProfile,
        'userOrders': userOrders,
        'orderItems': orderItems,
        'form':form
    }

    return render(request, 'store/profile.html', context)

@custom_login_required
def changePasswordView(request):
    if request.method == 'POST':
        form = UpdatePassword(user=request.user, data=request.POST)
        if form.is_valid():
            user = forms.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated')
            return redirect('profile')
        else:
            messages.error(request, 'Erro')
    else:
        form = UpdatePassword(user = request.user)
    
    return render(request, 'store/modal_password.html', {'form':form})



