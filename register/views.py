from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def register(request):
    template = loader.get_template('signup.htm')
    return HttpResponse(template.render())