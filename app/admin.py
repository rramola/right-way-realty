from django.contrib import admin
from .models import *

class RentalImageInline(admin.TabularInline):
    model = RentalImage
    extra = 1  # Number of empty forms to display

class RentalAdmin(admin.ModelAdmin):
    list_display = (
        'street_name',
        'city',
        'state',
        'postal_code',
        'rental_price',
        'available_from',
        'bedrooms',
        'baths',
        'fenced_yard',
    )
    search_fields = ('street_name', 'city', 'state', 'postal_code', 'rental_price')
    list_filter = ('bedrooms', 'baths', 'fenced_yard')
    ordering = ('-available_from',)
    inlines = [RentalImageInline]  # Include images inline in the rental admin form

admin.site.register(Rental, RentalAdmin)

