from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()

class User(models.Model):

    username = models.FloatField(null=True, blank=True, default=None)
    password = models.FloatField(null=True, blank=True, default=None)
    email = models.CharField(max_length=250)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='restaurant')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('name',)
        app_label = 'YourPrivateRestaurantDesigner'

    def __str__(self):
        return self.username