import requests
from django.core.management.base import BaseCommand
from app.navica import NavicaAPI
from app.models import Property
import os
import pprint

class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'

    def handle(self, *args, **kwargs):
        token = "0d56bf44bf5c56b3e3c645c5804e4337"
        def replace_placeholder(value):
                    if value == '*':
                        return None
                    return value
        
        def convert_to_decimal(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None
        if not token:
            self.stdout.write(self.style.ERROR('API token is not set in environment variables'))
            return
        api = NavicaAPI(token)

        try:
            listing_data = api.get_properties(endpoint='listings')   
            pp = pprint.PrettyPrinter(indent=2)

            
            data = listing_data['bundle']
        
            for listing in data:
                Property.objects.update_or_create(
                    mls_number = listing["ListingId"],
                      defaults={
                        'list_price': convert_to_decimal(replace_placeholder(listing.get('ListPrice'))),
                        'house_number': replace_placeholder(listing.get('StreetNumber')),
                        'street_name': replace_placeholder(listing.get('StreetName')),
                        'street_suffix': replace_placeholder(listing.get('StreetSuffix')),
                        'city': replace_placeholder(listing.get('City')),
                        'state': replace_placeholder(listing.get('StateOrProvince')),
                        'postal_code': replace_placeholder(listing.get('PostalCode')),
                        'description': replace_placeholder(listing.get('PublicRemarks')),
                        'latitude': convert_to_decimal(replace_placeholder(listing.get('Latitude'))),
                        'longitude': convert_to_decimal(replace_placeholder(listing.get('Longitude'))),
                        'year_built': convert_to_decimal(replace_placeholder(listing.get('YearBuilt'))),
                        'bedrooms': listing.get('BedroomsTotal',0),
                        'baths_full': convert_to_decimal(replace_placeholder(listing.get('BathroomsFull'))),
                        'baths_half': convert_to_decimal(replace_placeholder(listing.get('BathroomsHalf'))),
                        'baths_total': listing.get('BathroomsTotalDecimal', 0),
                        'baths_three_quarter': convert_to_decimal(replace_placeholder(listing.get('BathsThreeQuarter'))),
                        'building_area_total': convert_to_decimal(replace_placeholder(listing.get('BuildingAreaTotal'))),
                        'public_remarks': replace_placeholder(listing.get('PublicRemarks')),
                        'private_remarks': replace_placeholder(listing.get('PrivateRemarks')),
                        'property_subtype': replace_placeholder(listing.get('PropertySubType')),
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))