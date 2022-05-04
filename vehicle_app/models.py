from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='userprofile')


    def __str__(self):
        return '{}'.format(self.user.username)


class AllVehicles(models.Model):
    v_types = [('Motor cycle', 'Motor cycle'), ('Car', 'Car'), ('Truck', 'Truck'), ('bycycle', 'bycycle'),
               ('auto rickshaw', 'auto rickshaw'), ]
    t_types = [('el', 'electrical'), ('pl', 'petrol'), ('dl', 'diesel'), ]
    vehicletype = models.CharField(max_length=150, blank=False, choices=v_types)
    t_type = models.CharField(max_length=150, blank=False, choices=t_types)
    v_name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank=False)
    v_img = models.ImageField(upload_to='vehicle', blank=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('v_name',)
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def get_url(self): # for dropdown selection
        return reverse('vehicle_app:product_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.v_name)
