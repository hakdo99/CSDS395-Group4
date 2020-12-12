from django.urls import path
from . import views

urlpatterns = [
    path('myrestaurant', views.restaurantView, name='restaurantView'),
    path('', views.mainPage, name='mainPage'),
    path('addsect', views.addSection, name='addSection'),
    path('addvid', views.addVideo, name='addVideo'),
    path('sections', views.getSections, name='getSections')
]
