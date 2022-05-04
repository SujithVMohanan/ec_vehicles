from django.shortcuts import render
from vehicle_app.models import AllVehicles
# Create your views here.

def details(request,pk):
    try:
        vehicle = AllVehicles.objects.get(pk=pk)
        print(vehicle)
    except Exception as e:
        raise e
    return render(request,'details.html', {'vehicle':vehicle})