from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'product_app'

urlpatterns = [
    path('<int:pk>/', views.details, name='detail')
]