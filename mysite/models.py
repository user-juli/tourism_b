from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils.text  import slugify

class Place(models.Model):
    class Category(models.TextChoices):
        RIVER = 'RI', _('River')
        BEACG = 'BE', _('Beach')
        CITY = 'CI', _('City')

    title = models.CharField(max_length=200)
    text = RichTextField()
    category = models.CharField(max_length=2,choices=Category.choices,default=Category.RIVER,)
    image_header = models.ImageField(upload_to='destinations/', default = 'destinations/None/no-img.jpg')
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.category)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Place, self).save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image_header.url
        except:
            url = ''
        return url

def upload_gallery_image(instance, filename):
    return f"places/{instance.place.title}/{filename}"

class ImagesPlace(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.image.url))
        else:
            return '(No image)'

class Hotel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image_header = models.ImageField(upload_to='hotels/', default = 'hotels/None/no-img.jpg')
    minimal_price = models.IntegerField()
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Hotel, self).save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image_header.url
        except:
            url = ''
        return url

def upload_gallery_hotel(instance, filename):
    return f"hotels/{instance.hotel.title}/{filename}"

class ImagesHotel(models.Model):
    image = models.ImageField(upload_to=upload_gallery_hotel)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.image.url))
        else:
            return '(No image)'

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

class Activity(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    image_header = models.ImageField(upload_to='activities/', default = 'activities/None/no-img.jpg')
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.image_header)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Activity, self).save(*args, **kwargs)
