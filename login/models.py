from django.db import models

# Create your models here.
class userAccount(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
