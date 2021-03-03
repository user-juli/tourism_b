from django.shortcuts import render
from .models import Destination,Hotel,Restaurant

def index(request):
    return render(request,'mysite/index.html')

def information(request):
    return render(request,'mysite/information.html')

def contact(request):
    return render(request,'mysite/contact.html')

def map(request):
    return render(request,'mysite/map.html')

def destination(request):
    destinations = Destination.objects.all()
    return render(request,'mysite/destinations.html',{'destinations':destinations})

def rivers(request):
    rivers = Destination.objects.filter(category='RI')
    return render(request,'mysite/rivers.html',{'rivers':rivers})

def beaches(request):
    beaches = Destination.objects.filter(category='BE')
    return render(request,'mysite/beaches.html',{'beaches':beaches})

def hotel(request):
    hotels = Hotel.objects.all()
    return render(request,'mysite/hotels.html',{'hotels':hotels})

def restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request,'mysite/restaurants.html',{'restaurants':restaurants})
