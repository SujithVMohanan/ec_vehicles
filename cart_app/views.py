from django.shortcuts import render, redirect
from .models import Cart
from vehicle_app.models import AllVehicles


# Create your views here.

def addtocart(request, pk):
    product = AllVehicles.objects.all().get(id=pk)
    print(product.price)
    if request.user.is_authenticated:
        try:
            items = Cart.objects.create(user=request.user, item=product)
            items.save()
        except:
            print('uuuuuuuuuu')
            # items = Cart.objects.create(user=request.user, item=product)
            # items.save()

    return redirect('cart_app:cart_details')


def cart_details(request, total=0, ):
    if request.user.is_authenticated:
        user = request.user
        cart_items = Cart.objects.all().filter(user=user)
        total_items = len(cart_items)
        for cart in cart_items:
            total += cart.item.price

    return render(request, 'cart.html', {'item': cart_items, 'total': total, 'items': total_items})


def delete_cart(request, pid):
    if request.user.is_authenticated:
        cart_item = Cart.objects.all().filter(id=pid)
        print(cart_item)
        cart_item.delete()

    return redirect('cart_app:cart_details')