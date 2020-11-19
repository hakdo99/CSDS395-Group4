from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant


# Create your views here.
def showRestaurant(request):
    res_list = Restaurant.objects.all()
    html = ''
    for restaurant in res_list:
        url = '/restaurant/' + str(restaurant.name) + '/'
        html += '<a href="' + url +'">' + restaurant.name + '</a><br>'

    return HttpResponse(html)

def details(request, name):
    return HttpResponse("<h2> details for restaurant " + name + "<h2>")