from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Section
import logging
import sys

# Get an instance of a logger
logger = logging.getLogger('homepage')
current_id = None

# Create your views here.
def mainPage(request):
    sections = Section.objects.filter(tag='div')
    return render(request, 'homepage.html', {'section': 'homepage', 'sects' : sections})

def getSections(request):
    sections = Section.objects.filter(tag='div')
    return render(request, 'page.html', {'sects' : sections})

def addSection(request):
    global current_id
    section = Section(tag='div', parent=None)
    logger.debug(f'created {str(section)}')
    section.save()
    current_id = section.id
    sections = Section.objects.filter(tag='div')
    return render(request, 'page.html', {'sects' : sections, 'curr_sect': section.id})

def addVideo(request):
    """
    Add video as a section
    """
    if request.is_ajax():
        curr = request.POST.get('sect_id', None) # getting data from first_name input 
        height = request.POST.get('height', None)  # getting data from last_name input
        width = request.POST.get('width', None)
        link = request.POST.get('link', None)
        print(curr, height, width, link)
        parent = Section.objects.filter(id=current_id)[0]
        video = Section(tag='video', height=height, width=width,
                        link=link, parent=parent)
        video.save()
    sections = Section.objects.filter(tag='div')
    return render(request, 'page.html', {'sects' : sections, 'curr_sect': current_id})    

def restaurantView(request):
    return HttpResponse("Restaurant manager homepage")

def deleteSection(request):
    if request.method == "POST" and request.is_ajax():
        current_id = request.POST.get('id', None)
        print(current_id)
        current_sect = Section.objects.filter(id=current_id)
        current_sect.delete()
        return render(request, 'page.html', {'section': 'order', 'sects': Section.objects.all()})
    else:
        return None
    
def render_preview(request):
    return render(request, 'rendered_homepage.html', {'section': 'order', 'sects': Section.objects.filter(tag='div')})