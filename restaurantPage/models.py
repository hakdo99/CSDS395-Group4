from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    restaurant_logo = models.ImageField()
    restaurant_photo = models.ImageField()


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Menu_Item(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=250)
    item_photo = models.ImageField()


