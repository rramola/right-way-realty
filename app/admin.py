from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('mls_number', 'list_price', 'house_number', 'street_name', 'bedrooms', 'baths', 'subdivision', 'city')
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
