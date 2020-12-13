from django.db import models

# Create your models here.

class Order(models.Model):
    ordernum = models.CharField(max_length=250)