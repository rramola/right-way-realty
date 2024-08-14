from django.shortcuts import render, redirect
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
    context = {"properties": properties}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def property_list(request):
    properties = Property.objects.all()
    return render(request, "properties.html", {"properties": properties})


def googlemaps_view(request):
    properties = Property.objects.all()
    return render(request, "googlemaps.html", {"properties": properties})


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
