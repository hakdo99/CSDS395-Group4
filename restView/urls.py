from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.index, name='index'),
    path('edit', views.index, name='index'),
    path('', views.index, name='index'),
]