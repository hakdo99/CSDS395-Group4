from django.urls import path
from . import views
from login.views import user_login

urlpatterns = [
    path('myrestaurant', views.restaurantView, name='restaurantView'),
    path('home', views.mainPage, name='mainPage'),
    path('addsect', views.addSection, name='addSection'),
    path('addvid', views.addVideo, name='addVideo'),
    path('sections', views.getSections, name='getSections'),
    path('', user_login, name='initialPage'),
]
