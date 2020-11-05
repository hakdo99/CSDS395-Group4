from django.urls import path
from . import views

urlpatterns = [
    path('', views.resCreate, name='resCreate'),
    path('menu/', views.menu, name= 'resMenu'),
    path('location/', views.location, name='resLocate'),
]