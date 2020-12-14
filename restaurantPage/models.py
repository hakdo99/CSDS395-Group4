from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    restaurant_logo = models.ImageField()
    restaurant_photo = models.ImageField()





