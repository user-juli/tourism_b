from django.db import models
from django.utils import timezone

RIVER = 'RI'
BEACH = 'BE'
CITY = 'CI'
UNKNOWN = 'UN'
CATEGORY_CHOICES = [
    (RIVER, 'River'),
    (BEACH, 'Beach'),
    (CITY, 'City'),
    (UNKNOWN, 'Unknown'),
]

class Destination(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=UNKNOWN,)
    ##image = models.ImageField(upload_to='uploads/', default = 'uploads/None/no-img.jpg')

    def __str__(self):
        return self.title

def upload_gallery_image(instance, filename):
    return f"images/{instance.destination.title}/gallery/{filename}"

class Image_Destination(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="images")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Hotel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/', default = 'uploads/None/no-img.jpg')

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Restaurant(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/', default = 'uploads/None/no-img.jpg')

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
