from django.shortcuts import render
from django.http import HttpResponse
from .models import Section


# Create your views here.
def order(request):
    return render(request, 'order.html', {'section': 'order', 'sects': Section.objects.all()})

def add_button(request):
    if request.method == "POST" and request.is_ajax():
        link = request.POST.get('link', None)
        text = request.POST.get('text', None)
        print(link, text)
        new_section = Section(tag="button", text=text, link=link, parent=None)
        new_section.save()
        return render(request, 'order.html', {'section': 'order'})
    else:
        return None

def get_sections(request):
    return render(request, 'order_page.html', {'section': 'order', 'sects': Section.objects.all()})

def delete_sections(request):
    if request.method == "POST" and request.is_ajax():
        current_id = request.POST.get('id', None)
        print(current_id)
        current_sect = Section.objects.filter(id=current_id)
        current_sect.delete()
        return render(request, 'order_page.html', {'section': 'order', 'sects': Section.objects.all()})
    else:
        return None

def render_preview(request):
    return render(request, 'rendered_order.html', {'section': 'order', 'sects': Section.objects.all()})



