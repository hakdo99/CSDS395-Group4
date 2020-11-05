from django.urls import path
from . import views

urlpatterns = [
    path('customerView', views.customerView, name='customerView'),
    path('', views.index, name='index'),

]
