from django.urls import path
from . import views

app_name = 'vehicle_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('reg/', views.reg, name='reg'),
    path('logout', views.logout, name='logout'),
    path('<slug:c_slug>/', views.home, name='product_by_category'),
]