from django.db import models

# Create your models here.

class Order(models.Model):
    ordernum = models.CharField(max_length=250)

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    text = models.CharField(max_length=400, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=400, blank=True, null=True)
    is_left = models.CharField(max_length=30, blank=True, null=True)
    style = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True) 
    parent = models.ForeignKey('self', null=True, blank=True, 
                                    on_delete=models.CASCADE, related_name='children') 