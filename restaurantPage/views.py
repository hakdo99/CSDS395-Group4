from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def showRestaurant(request):
    return HttpResponse("<h1>Restaurant homepage</h1>")