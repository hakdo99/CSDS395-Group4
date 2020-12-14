from django.db import models
from restaurantPage.models import Restaurant
# Create your models here.

class menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class menuItem(models.Model):
    resMenu = models.ForeignKey(menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=250)
    item_photo = models.ImageField()