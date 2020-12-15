from django.urls import path
from . import views
from homepage.views import mainPage
urlpatterns = [
    path('', views.register, name='register'),
    path('home/', mainPage, name='register redirect')
]