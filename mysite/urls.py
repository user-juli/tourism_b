from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rivers', views.rivers, name='rivers'),
    path('beaches', views.beaches, name='beaches'),
    path('information', views.information, name='information'),
    path('contact',views.contact,name='contact'),
    path('map',views.map,name='map'),
    path('destination', views.destination, name='destination'),
    path('hotel', views.hotel, name='hotel'),
    path('restaurant', views.restaurant, name='restaurant'),
]
