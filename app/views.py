from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.urls import reverse
from django.db import connection
from datetime import date
from django.contrib.auth import logout
import random


# from populate_dummy_data import *
def home_page(request):
    # FETCH PROPERTIES
    property_list = []
    try:
        properties = Property.objects.filter(city='Oxford').iterator(chunk_size=100)
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

    # Randomize properties
    list_of_nums = []
    list_len = len(property_list) - 1
    while len(list_of_nums) < 3:
        rand = random.randint(0,list_len)
        if rand not in list_of_nums:
            list_of_nums.append(rand)

    # Add properties to new list
    display_properties = []
    display_properties.append(property_list[list_of_nums[0]])
    display_properties.append(property_list[list_of_nums[1]])
    display_properties.append(property_list[list_of_nums[2]])

    # Random property image lists   
    # prop_one_images = PropertyImage.objects.filter(property=display_properties[0])
    # prop_two_images = PropertyImage.objects.filter(property=display_properties[1])
    # prop_three_images = PropertyImage.objects.filter(property=display_properties[2])
    


    context = {
        'list': list_of_nums,
        'properties': display_properties
        # 'prop_one_images': prop_one_images,
        # 'prop_two_images' : prop_two_images,
        # 'prop_three_images': prop_three_images
    }
    return render(request, "home.html", context)


def about_page(request):
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

            return render(request, "about.html")
    else:
        form = ContactForm()
    return render(request, "about.html", {"form": form})

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

    context = {
        'property': property,
        'baths_info': baths_total,
        'images': images,
        'form': form,
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


def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_number = form.cleaned_data.get('phone_number')
            ##################EMAIL##############################
            htmly = get_template('email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'title': 'register here'
    }
    return render(request, "register_page.html", context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username} !')
            return redirect('home')
        else:
            messages.info(request, f'Username or Password invalid. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, "login_page.html", {'form': form,
        'title': 'log in'})

def profile_page(request):
    return render(request, "profile.html")

def logout_view(request):
    logout(request)
    return redirect('login')