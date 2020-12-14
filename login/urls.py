from django.urls import  include, path
from . import views
from homepage.views import mainPage

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/', views.forgotPassword, name='forgotPassword'),
    path('loggedin/', mainPage, name='log in transfer'),
    path('reset/', views.resetPassword, name='resetPassword'),
]