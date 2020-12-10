from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def login(request):
    return render(request, 'index.htm', {'section': 'login'})

def logout(request):
    return render(request, 'logout.html', {'section': 'logout'})

def forgotPassword(request):
    return HttpResponse("password recovery page")
