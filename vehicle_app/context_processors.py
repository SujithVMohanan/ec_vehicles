from . models import AllVehicles


def menu_link(request):
    link = AllVehicles.objects.all()
    return dict(link=link)
