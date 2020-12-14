from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order, name='order'),
    path('addbutton', views.add_button, name='addButton'),
    path('getsects', views.get_sections, name='getOrderSections'),
    path('deletesects', views.delete_sections, name='deleteSections')
]
