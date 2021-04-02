from django.contrib import admin
from . models import Place,Hotel,Restaurant,ImagesPlace,Activity,ImagesHotel,ImagesActivity


admin.site.register(Restaurant)

class ImageInline(admin.TabularInline):
    model = ImagesPlace
    readonly_fields = ('image_preview',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'image_header')
    inlines = [
        ImageInline
    ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(PlaceAdmin, self).get_form(request, obj, **kwargs)
        return form

class ImageInlineHotel(admin.TabularInline):
    model = ImagesHotel
    readonly_fields = ('image_preview',)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_header')
    inlines = [
        ImageInlineHotel
    ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(HotelAdmin, self).get_form(request, obj, **kwargs)
        return form

class ImageInlineActivity(admin.TabularInline):
    model = ImagesActivity
    readonly_fields = ('image_preview',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_header')
    inlines = [
        ImageInlineActivity
    ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(ActivityAdmin, self).get_form(request, obj, **kwargs)
        return form
