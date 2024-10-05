import requests
from django.core.management.base import BaseCommand
from navica import NavicaAPI
from models import NavicaProperty
import os


class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'

    def fetch_navica_data_from_api(self):
        token = os.getenv("0d56bf44bf5c56b3e3c645c5804e4337")
        if not token:
            self.stdout.write(self.style.ERROR('API token is not set in environment variables'))
            return
        api = NavicaAPI(token)

        try:
            listing_data = api.get_properties(endpoint='listings')   
            properties = listing_data['bundle']
            for listing in properties:
                NavicaProperty.objects.update_or_create(
                    SourceSystemKey = listing["SourceSystemKey"],
                    defaults={
                        'BedroomsTotal': listing['BedroomsTotal', 0],
                        'GarageYN': listing['GarageYN', False],
                        'Longitude': listing['Longitude'],
                        'Latitude': listing['Latitude'],
                        'PublicRemarks': listing['PublicRemarks', ''],
                        'CountyOrParish': listing['CountyOrParish', ''],
                        'BathroomsTotalDecimal': listing['BathroomsTotalDecimal', 0],
                        'ListPrice': listing['ListPrice', 0],
                        'UnparsedAddress': listing['UnparsedAddress', ''],
                        'YearBuilt': listing['YearBuilt', None],
                        'HighSchoolDistrict': listing['HighSchoolDistrict', ''],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))