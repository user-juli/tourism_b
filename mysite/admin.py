from django.contrib import admin
from . models import Destination,Hotel,Restaurant,Image_Destination

#admin.site.register(Destination)
admin.site.register(Hotel)
admin.site.register(Restaurant)

class ImageInline(admin.TabularInline):
    model = Image_Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
