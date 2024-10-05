import requests
from django.core.management.base import BaseCommand
from app.navica import NavicaAPI
from app.models import NavicaProperty
import os
import pprint

class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'

    def handle(self, *args, **kwargs):
        token = "0d56bf44bf5c56b3e3c645c5804e4337"
        if not token:
            self.stdout.write(self.style.ERROR('API token is not set in environment variables'))
            return
        api = NavicaAPI(token)

        try:
            listing_data = api.get_properties(endpoint='listings')   
            pp = pprint.PrettyPrinter(indent=2)

            
            properties = listing_data['bundle']
            for listing in properties:
                NavicaProperty.objects.update_or_create(
                    SourceSystemKey = listing["SourceSystemKey"],
                    defaults={
                        'BedroomsTotal': listing.get('BedroomsTotal', 0),
                        'GarageYN': listing.get('GarageYN', False),
                        'Longitude': listing.get('Longitude'),
                        'Latitude': listing.get('Latitude'),
                        'PublicRemarks': listing.get('PublicRemarks', ''),
                        'CountyOrParish': listing.get('CountyOrParish', ''),
                        'BathroomsTotalDecimal': listing.get('BathroomsTotalDecimal', 0),
                        'ListPrice': listing.get('ListPrice', 0),
                        'UnparsedAddress': listing.get('UnparsedAddress', ''),
                        'YearBuilt': listing.get('YearBuilt', None),
                        'HighSchoolDistrict': listing.get('HighSchoolDistrict', ''),
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))