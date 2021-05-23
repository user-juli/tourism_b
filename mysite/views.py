from django.shortcuts import render, redirect, get_object_or_404
from .models import Place,Hotel,Restaurant,Activity,ImagesPlace,ImagesHotel,ImagesActivity
from django.views.generic import DetailView,ListView
from django.http import HttpResponse

from posts.models import Post

class IndexFeedView(ListView):
    template_name = 'mysite/index.html'
    model = Post
    context_object_name = 'blogs'
    queryset = Post.objects.all().order_by('-id')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activity.objects.all().order_by('-id')
        return context


def information(request):
    return render(request,'mysite/information.html')

def history(request):
    return render(request, 'mysite/history.html')

def contact(request):
    return render(request,'mysite/contact.html')

def map(request):
    return render(request,'mysite/map.html')

def howtoget(request):
    return render(request, 'mysite/howtoget.html')


def destination(request):
    places = Place.objects.all()
    return render(request,'mysite/destinations.html',{'places':places})

def rivers(request):
    rivers = Place.objects.filter(category='RI')
    return render(request,'mysite/rivers.html',{'rivers':rivers})

def beaches(request):
    beaches = Place.objects.filter(category='BE')
    return render(request,'mysite/beaches.html',{'beaches':beaches})

def restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request,'mysite/restaurants.html',{'restaurants':restaurants})

class PlaceDetailView(DetailView):
    template_name = 'mysite/detail_d.html'
    model = Place
    context_object_name = 'place'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_queryset(self):
        return self.model.objects.filter(url=self.kwargs['url'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagesplace'] = ImagesPlace.objects.filter(place=self.get_object()).all()
        return context

class HotelFeedView(ListView):
    template_name = 'mysite/hotels.html'
    model = Hotel
    ordering = ('-minimal_price',)
    paginate_by = 5
    context_object_name = 'hotels'
    queryset = Hotel.objects.all()

class HotelDetailView(DetailView):
    template_name = 'mysite/detail_h.html'
    model = Hotel
    context_object_name = 'hotel'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_queryset(self):
        return self.model.objects.filter(url=self.kwargs['url'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imageshotel'] = ImagesHotel.objects.filter(hotel=self.get_object()).all()
        context['hotels'] = Hotel.objects.filter(minimal_price)
        return context
