from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def login(request):
    template = loader.get_template('ind.htm')
    return HttpResponse(template.render())

def forgotPassword(request):
    return HttpResponse("password recovery page")
