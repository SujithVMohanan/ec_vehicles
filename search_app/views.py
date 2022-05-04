from django.db.models import Q
from django.shortcuts import render
from vehicle_app.models import AllVehicles

# Create your views here.

def search(request):
    product = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = AllVehicles.objects.all().filter(Q(v_name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html',{'query':query, 'products':product} )