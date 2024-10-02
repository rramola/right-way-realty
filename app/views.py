from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.urls import reverse

# from populate_dummy_data import *


def home_page(request):
    properties = Property.objects.all()

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

            
    context = {"properties": properties}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)

def oxford_page(request):
    context = {}
    return render(request, "oxford.html", context)

def googlemaps_view(request):
    properties = Property.objects.all()
    
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
    
    return render(request, "googlemaps.html", {"properties": properties})

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    full_baths = float(property.baths_full or 0)
    half_baths = float(property.baths_half or 0)

    if half_baths > 1:
        baths_info = f"{full_baths} Full, {half_baths} Half Baths"
    elif half_baths > 0:
        total_baths = full_baths + (half_baths / 2)
        baths_info = f"{total_baths:.1f}"
    else:
        baths_info = f"{full_baths:.1f}"

    context = {
        'property': property,
        'baths_info': baths_info,
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
