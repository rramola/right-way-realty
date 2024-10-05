import requests
from django.core.management.base import BaseCommand
from .models import NavicaProperty
import os


class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'

    def fetch_navica_data_from_api(self):
        api_url = "https://navapi.navicamls.net/api/v2/nav98/listings?"
        token = os.getenv("0d56bf44bf5c56b3e3c645c5804e4337")
        if not token:
            self.stdout.write(self.style.ERROR('API token is not set in environment variables'))
            return
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            listings = response.json()
            properties = listings['bundle']
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
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from the API'))

