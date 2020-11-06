from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def resCreate(request):
    return HttpResponse("<h1>Restaurant creation/editing homepage</h1>")

def menu(request):
    return HttpResponse("<h1>Restaurant menu page</h1>")

def location(request):
    return HttpResponse("<h1>Restaurant Location page</h1>")