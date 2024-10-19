from django.core.management.base import BaseCommand
from rets import Session
from app.models import Property
from decimal import Decimal


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

                # Fetch class metadata for the Property resource
                class_metadata = session.get_class_metadata(resource='Property')
                self.stdout.write(self.style.SUCCESS(f'Class metadata fetched: {class_metadata}'))
                
                # Fetch table metadata for the Residential class
                table_metadata = session.get_table_metadata(resource='Property', resource_class="A")

                # Define a DMQL query to fetch active property data
                dmql_query = "(LIST_15=A)"  # Ensure 'A' corresponds to active listings

                # Fetch property data using the DMQL query
                properties = list(session.search('Property', resource_class='A', dmql_query=dmql_query))

                # Check if properties were fetched
                if not properties:
                    self.stdout.write(self.style.WARNING('No properties found for the given query'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Found {len(properties)} properties'))

                # Store fetched properties into the database
                for prop in properties:
                    try:
                        # Create or update Property instance
                        property_instance, created = Property.objects.update_or_create(
                            mls_number=prop['MLSNumber'],  # Adjust based on your actual property field
                            defaults={
                                'list_price': Decimal(prop['ListPrice']) if prop['ListPrice'] else None,
                                'subdivision_name': prop.get('SubdivisionName', ''),
                                'house_number': prop.get('HouseNumber', ''),
                                'street_name': prop.get('StreetName', ''),
                                'street_suffix': prop.get('StreetSuffix', ''),
                                'city': prop.get('City', ''),
                                'state': prop.get('State', ''),
                                'postal_code': prop.get('PostalCode', ''),
                                'description': prop.get('Description', ''),
                                'latitude': prop.get('Latitude', None),
                                'longitude': prop.get('Longitude', None),
                                'year_built': prop.get('YearBuilt', None),
                                'bedrooms': prop.get('Bedrooms', None),
                                'baths_full': prop.get('BathsFull', None),
                                'baths_half': prop.get('BathsHalf', None),
                                'baths_total_integer': prop.get('BathsTotalInteger', None),
                                'baths_total': prop.get('BathsTotal', None),
                                'carport': bool(prop.get('Carport', False)),
                                # Add more fields as needed
                            }
                        )
                        self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} property: {property_instance.mls_number}"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error processing property: {e}"))
                        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error logging in or fetching data: {e}"))
