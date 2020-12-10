from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def menu(request):
    return render(request, 'menu.html', {'section': 'menu'})