from django.urls import path
from . import views

app_name ='cart_app'

urlpatterns = [
    path('cartD/', views.cart_details, name='cart_details'),
    path('remove/<int:pid>/', views.delete_cart, name='remove_cart'),
    path('add/<int:pk>/', views.addtocart, name='addcart'),
]