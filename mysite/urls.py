from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rivers', views.rivers, name='rivers'),
    path('beaches', views.beaches, name='beaches'),
    path('information', views.information, name='information'),
    path('destination', views.destination, name='destination'),
]
