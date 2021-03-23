from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rivers', views.rivers, name='rivers'),
    path('beaches', views.beaches, name='beaches'),
    path('information', views.information, name='information'),
    path('history', views.history, name='history'),
    path('contact',views.contact,name='contact'),
    path('map',views.map,name='map'),
    path('howtoget',views.howtoget,name='howtoget'),
    path('destination', views.destination, name='destination'),
    path('hotel', views.hotel, name='hotel'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('destination/<slug:url>/',views.PlaceDetailView.as_view(),name='detail'),
    path('hotel/<slug:url>/',views.HotelDetailView.as_view(),name='detail'),
]
