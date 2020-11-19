from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showRestaurant, name='showRestaurant'),
    path('edit/', include("restaurantCreate.urls")),
    path('<str:name>/', views.details, name='details')
]