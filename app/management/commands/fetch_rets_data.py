import os
from django.core.management.base import BaseCommand
from rets import Session
from app.models import Property

class Command(BaseCommand):
    help = 'Fetches and stores property data from the Flexmls RETS API.'

    def handle(self, *args, **kwargs):
        rets_url = "http://retsgw.flexmls.com:80/rets2_3/Login"
        rets_username = "tup.rets.rightway"
        rets_password = "kW-1kfycng"

        # Initialize RETS session
        session = Session(rets_url, rets_username, rets_password)

        try:
            # Log in to RETS
            if session.login():
                self.stdout.write(self.style.SUCCESS('Successfully logged in to RETS'))

                # Fetch resource metadata
                resources = session.get_resource_metadata(resource='Property')
                self.stdout.write(self.style.SUCCESS(f'Resources metadata fetched: {resources}'))

                # Fetch class metadata for the Property resource
                class_metadata = session.get_class_metadata(resource='Property')
                self.stdout.write(self.style.SUCCESS(f'Class metadata fetched: {class_metadata}'))

                # Fetch table metadata for the Residential class
                table_metadata = session.get_table_metadata(resource='Property', resource_class="A")
                self.stdout.write(self.style.SUCCESS(f'Table metadata fetched: {table_metadata}'))

                # Define a DMQL query to fetch property data (e.g., all active properties)
                dmql_query = "(Status=A)"

                # Fetch property data using the DMQL query
                properties = session.search('Property', resource_class='A', dmql_query=dmql_query)

                # Store fetched properties into the database
                for prop in properties:
                    # Create or update the property record
                    Property.objects.update_or_create(
                        mls_number=prop['MLS'],
                        defaults={
                            'list_price': prop.get('Price'),
                            'bedrooms': prop.get('Bedrooms'),
                            'baths_full': prop.get('BathsFull'),
                            'baths_half': prop.get('BathsHalf'), 
                            'house_number': prop.get('Address').split()[0] if prop.get('Address') else None,
                            'street_name': ' '.join(prop.get('Address').split()[1:-1]) if prop.get('Address') else None,
                            'street_suffix': prop.get('Address').split()[-1] if prop.get('Address') else None,
                            'city': prop.get('City'),
                            'state': prop.get('State'),
                            'postal_code': prop.get('PostalCode'),
                            'year_built': prop.get('YearBuilt'),
                            'public_remarks': prop.get('PublicRemarks'),
                            'private_remarks': prop.get('PrivateRemarks'),
                            'latitude': prop.get('Latitude'),
                            'longitude': prop.get('Longitude'),
                            'building_area_total': prop.get('BuildingAreaTotal'),
                            'property_subtype': prop.get('PropertySubtype'),
                            # Add other fields as necessary
                        }
                    )
                self.stdout.write(self.style.SUCCESS('Successfully fetched and stored property data'))

            else:
                self.stdout.write(self.style.ERROR('Login to RETS failed'))

        except Exception as e:
            self.stdout
