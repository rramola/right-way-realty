from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import *
# from .forms import *
# from populate_dummy_data import *
# Create your views here.


def home_page(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties.html', {'properties': properties})

# def add_property(request):
#     myForm = AddPropertyForm()
#     if request.method == "POST":
#         myForm = AddPropertyForm()
#         if myForm.is_valid():
#             mls_number = myForm.cleaned_data.get('mls_number')
#             list_price = myForm.cleaned_data.get('list_price')
#             house_number = myForm.cleaned_data.get('house_number')
#             street_name = myForm.cleaned_data.get('street_name')
#             bedrooms = myForm.cleaned_data.get('bedrooms')
#             bath = myForm.cleaned_data.get('bath')
#             subdivision = myForm.cleaned_data.get('subdivision')
#             cities = myForm.cleaned_data.get('cities')
#             description = myForm.cleaned_data.get('description')
#             image = myForm.cleaned_data.get('image')
#             create_dummy_properties(mls_number, list_price,house_number, street_name,bedrooms, bath, subdivision, cities, description, image)
#             return redirect("home.html")
#     context = {"form": myForm}
#     return render(request, "add_property.html", context )


def contact_page(request):
    context = {}
    return render(request, "contact.html", context)
