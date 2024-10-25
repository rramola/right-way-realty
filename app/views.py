from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.urls import reverse
from django.db import connection
from datetime import date


# from populate_dummy_data import *
def home_page(request):
    property_list = []
    try:
        properties = Property.objects.all().iterator(chunk_size=100)
        property_list = list(properties)
    except Exception as e:
        print(f"Error retrieving properties: {e}")
        connection.close()
        try:
            properties = Property.objects.all().iterator(chunk_size=100)
            property_list = list(properties)  # Convert the iterator to a list
        except Exception as inner_e:
            print(f"Error retrieving properties again: {inner_e}")

    for property in properties:
        full_baths = float(property.baths_full or 0)
        half_baths = float(property.baths_half or 0)

        if half_baths > 1:
            property.baths_info = f"{full_baths} Full, {half_baths} Half Baths"
        elif half_baths > 0:
            total_baths = full_baths + (half_baths / 2)
            property.baths_info = f"{total_baths:.1f}"
        else:
            property.baths_info = f"{full_baths:.1f}"
        property_list.append(property)
    
    return render(request, "home.html", {"properties": property_list})


def about_page(request):
    context = {}
    return render(request, "about.html", context)

def oxford_page(request):
    context = {}
    return render(request, "oxford.html", context)

def googlemaps_view(request):
    property_list = []
    try:
        properties = Property.objects.all().iterator(chunk_size=100)
        property_list = list(properties)
    except Exception as e:
        print(f"Error retrieving properties: {e}")
        connection.close()
        try:
            properties = Property.objects.all().iterator(chunk_size=100)
            property_list = list(properties)  # Convert the iterator to a list
        except Exception as inner_e:
            print(f"Error retrieving properties again: {inner_e}")

        property_list.append(property)
    
    return render(request, "googlemaps.html", {"properties": property_list})

    
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    images = PropertyImage.objects.filter(property_id=property_id)
    full_baths = float(property.baths_full or 0)
    half_baths = float(property.baths_half or 0)
    baths_total = float(property.baths_total or 0)


    context = {
        'property': property,
        'baths_info': baths_total,
        'images': images
    }
    return render(request, 'properties.html', context)


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            recipient_list = ["ramolaryan@gmail.com"]
            try:
                send_mail(
                    subject=f"Contact Form Submission from {first_name} {last_name}",
                    message=f"Message from {first_name} {last_name} ({phone_number}, {email}):\n\n{message}",
                    from_email=email,
                    recipient_list=recipient_list,
                )
            except BadHeaderError:
                return HttpResponseBadRequest("Invalid header found.")

            return render(request, "home.html")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})



def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rental_list.html', {'rentals': rentals})

def load_more_properties(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 2))
    properties = Property.objects.all()[offset:offset + limit]

    property_list = []
    for property in properties:
        property_list.append({
            'id': property.id,
            'house_number': property.house_number,
            'street_name': property.street_name,
            'city': property.city,
            'state': property.state,
            'postal_code': property.postal_code,
            'list_price': property.list_price,
            'bedrooms': property.bedrooms,
            'baths_total': property.baths_total,
            'building_area_total': property.building_area_total,
            'property_type': property.property_type,
            'image_url': property.images.first().url if property.images.exists() else '',
            'latitude': property.latitude,
            'longitude': property.longitude,
        })

    return JsonResponse({'properties': property_list})


def filter_properties(request):
    mls_id = request.GET.get('mls_listing_id', '').strip()
    location_filter = request.GET.get('location', '').strip()
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', float('inf'))
    min_beds = request.GET.get('min_beds', 0)
    min_baths = request.GET.get('min_baths', 0)

    # Query properties based on filters
    properties = Property.objects.all()

    if mls_id:
        properties = properties.filter(mls_number=mls_id)

    if location_filter:
        properties = properties.filter(city__icontains=location_filter)

    if min_price:
        properties = properties.filter(list_price__gte=min_price)

    if max_price:
        properties = properties.filter(list_price__lte=max_price)

    if min_beds:
        properties = properties.filter(bedrooms__gte=min_beds)

    if min_baths:
        properties = properties.filter(baths_total__gte=min_baths)

    property_data = []
    for property in properties:
        property_data.append({
            'id': property.id,
            'latitude': property.latitude,
            'longitude': property.longitude,
            'house_number': property.house_number,
            'street_name': property.street_name,
            'city': property.city,
            'state': property.state,
            'postal_code': property.postal_code,
            'list_price': property.list_price,
            'bedrooms': property.bedrooms,
            'baths_total': property.baths_total,
            'building_area_total': property.building_area_total,
            'property_type': property.property_type,
            'image_url': property.images.first().url if property.images.exists() else '',
        })

    return JsonResponse({'properties': property_data})




