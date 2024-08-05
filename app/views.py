from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import *

# Create your views here.


def home_page(request):
    context = {}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties.html', {'properties': properties})


def contact_page(request):
    context = {}
    return render(request, "contact.html", context)
