from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register(request):
    return HttpResponse("<h1>new account page</h1>")