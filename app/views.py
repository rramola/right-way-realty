from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_page(request):
    context = {}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def properties_page(request):
    context = {}
    return render(request, "properties.html", context)


def contact_page(request):
    context = {}
    return render(request, "contact.html", context)
