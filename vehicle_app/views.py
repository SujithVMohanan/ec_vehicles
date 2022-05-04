from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import AllVehicles, UserProfile


# Create your views here.


def home(request, c_slug=None):
    c_page = None
    product_list = None
    if c_slug is not None:
        print('dffddfdfdfdfdf')
        print(c_slug)
        #c_page = get_object_or_404(AllVehicles, slug=c_slug)
        product_list = AllVehicles.objects.all().filter(slug=c_slug, available=True)
    else:
        print('dffddfdfdfdfdf')
        print(c_slug)
        product_list = AllVehicles.objects.all().filter(available=True)
    #paginator = Paginator(product_list, 6)
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except:
    #     page = 1
    # try:
    #     products = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     products = Paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'vehicle': product_list, 'category':c_page})


def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')

        print(email)
        print(password)

        user = authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect('/',)
        else:
            return redirect('/')

    return render(request, 'log.html', )

def logout(request):
    auth.logout(request)
    return redirect('/')

def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        c_Pass = request.POST.get('cpsw')

        if email != '':
            if password == c_Pass:
                if User.objects.all().filter(email=email).exists():
                    print('User is Exists')
                    return redirect('vehicle_app:reg')
                else:
                    user = User.objects.create_user(username=name, email=email, password=password)
                    user.save()
                    return redirect('/')
            else:
                print('password incorrect')
                return redirect('vehicle_app:reg')
        else:
            print('fields empty')
            return redirect('vehicle_app:reg')
    return render(request, 'register.html', )
