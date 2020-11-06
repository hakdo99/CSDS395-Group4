from django.urls import path
from . import views

urlpatterns = [
    path('myrestaurant', views.restaurantView, name='restaurantView'),
    path('', views.mainPage, name='mainPage'),

]
