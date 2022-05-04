from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AllVehicles, UserProfile



admin.site.register(UserProfile)

class AllVehicleAdmin(admin.ModelAdmin):
    list_display = ['v_name', 'slug', 't_type', 'vehicletype','v_img', 'desc', 'price','available']
    prepopulated_fields = {'slug': ('v_name',)}


admin.site.register(AllVehicles, AllVehicleAdmin)
