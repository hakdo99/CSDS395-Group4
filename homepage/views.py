from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Restaurant homepage</h1>")

def customerView(request):
    return HttpResponse("<h1>Customer homepage</h1>")

def restaurantView(request):
    return HttpResponse("Restaurant homepage")