import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'right_way_realty.settings')
django.setup()

from app.models import Property, PropertyImage

def create_dummy_properties():
    # Fetch existing MLS numbers to avoid duplicates
    existing_mls_numbers = set(Property.objects.values_list('mls_number', flat=True))
    
    mls_numbers = [f"MLS{1000+i}" for i in range(10)]
    list_prices = [250000, 450000, 750000, 1200000, 320000, 540000, 870000, 980000, 1100000, 1300000]
    house_numbers = [str(i) for i in range(1, 11)]
    street_names = [
        "Elm Street",
        "Oak Avenue",
        "Pine Road",
        "Maple Drive",
        "Birch Lane",
        "Cedar Court",
        "Spruce Street",
        "Walnut Way",
        "Willow Boulevard",
        "Redwood Circle"
    ]
    bedrooms = [2, 3, 4, 5, 3, 4, 3, 2, 4, 5]
    baths = [1.5, 2, 2.5, 3, 2, 2.5, 2, 1.5, 3, 3.5]
    subdivisions = [
        "Sunnyvale",
        "Greenfield",
        "Woodland",
        "Riverview",
        "Highland",
        "Lakeside",
        "Parkview",
        "Meadowbrook",
        "Brookside",
        "Hillside"
    ]
    cities = [
        "Springfield",
        "Riverside",
        "Greenville",
        "Fairview",
        "Madison",
        "Georgetown",
        "Clinton",
        "Franklin",
        "Bristol",
        "Salem"
    ]
    descriptions = [
        "A cozy cottage with a beautiful garden.",
        "A modern apartment in the heart of the city.",
        "A spacious villa with a private pool.",
        "A luxury penthouse with stunning views.",
        "A charming bungalow in a quiet neighborhood.",
        "A rustic cabin in the woods.",
        "An elegant townhouse with a garage.",
        "A beachfront condo with direct access to the beach.",
        "A mountain retreat with breathtaking views.",
        "An urban loft with an industrial vibe."
    ]

    for i in range(10):
        # Generate unique MLS number
        while mls_numbers[i] in existing_mls_numbers:
            mls_numbers[i] = f"MLS{random.randint(1000, 9999)}"
        existing_mls_numbers.add(mls_numbers[i])

        property = Property.objects.create(
            mls_number=mls_numbers[i],
            list_price=list_prices[i],
            house_number=house_numbers[i],
            street_name=street_names[i],
            bedrooms=bedrooms[i],
            baths=baths[i],
            subdivision=subdivisions[i],
            city=cities[i],
            description=descriptions[i]
        )

        # Add images to the property using PlaceKitten
        for j in range(3):
            PropertyImage.objects.create(
                property=property,
                image=f'https://placekitten.com/800/60{j}'
            )

if __name__ == "__main__":
    create_dummy_properties()
    print("Dummy properties with PlaceKitten images created successfully.")
