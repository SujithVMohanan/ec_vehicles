from django.contrib.auth.models import User
from django.db import models
from vehicle_app.models import AllVehicles


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(AllVehicles, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['item']
        verbose_name = 'Cart'
        verbose_name_plural ='Carts'

    def __str__(self):
        return '{}'.format(self.item)
