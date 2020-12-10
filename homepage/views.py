from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def mainPage(request):
    return render(request, 'homepage.html', {'section': 'homepage'})

def restaurantView(request):
    return HttpResponse("Restaurant manager homepage")