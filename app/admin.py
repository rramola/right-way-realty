from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'mls_number', 'list_price', 'house_number', 'street_name', 
        'street_suffix', 'city', 'state', 'postal_code', 'bedrooms', 
        'baths_full', 'baths_half', 'baths_three_quarter', 'building_area_total'
    )
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
