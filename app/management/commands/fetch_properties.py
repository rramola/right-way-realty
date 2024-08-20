from django.core.management.base import BaseCommand
from app.models import Property
from app.flexmls import FlexmlsAPI
import pprint

class Command(BaseCommand):
    help = 'Fetches properties from the Flexmls API and saves them to the database.'

    def handle(self, *args, **kwargs):
        access_token = 'b9vji5uevfyygmjhrjeico9jt'
        
        api = FlexmlsAPI(access_token)
        
        try:
            # Fetch data from the Flexmls API
            properties_data = api.get_properties(endpoint='listings')
            
            # # Pretty print the entire API response 
            # pp = pprint.PrettyPrinter(indent=2)
            # pp.pprint(properties_data)
            
            # Get the Results
            results = properties_data.get('D', {}).get('Results', [])
            
            # if results:
            #     pp.pprint(results[0])  # Print the first property data

            # Loop through the properties and save to the database
            for property_data in results:
                standard_fields = property_data.get('StandardFields', {})
                
                def replace_placeholder(value):
                    if value == '*':
                        return None
                    return value
                
                def convert_to_decimal(value):
                    try:
                        return float(value)
                    except (ValueError, TypeError):
                        return None

                Property.objects.update_or_create(
                    mls_number=standard_fields.get('ListingId'),
                    defaults={
                        'list_price': convert_to_decimal(replace_placeholder(standard_fields.get('ListPrice'))),
                        'house_number': replace_placeholder(standard_fields.get('StreetNumber')),
                        'street_name': replace_placeholder(standard_fields.get('StreetName')),
                        'street_suffix': replace_placeholder(standard_fields.get('StreetSuffix')),
                        'city': replace_placeholder(standard_fields.get('City')),
                        'state': replace_placeholder(standard_fields.get('StateOrProvince')),
                        'postal_code': replace_placeholder(standard_fields.get('PostalCode')),
                        'description': replace_placeholder(standard_fields.get('PublicRemarks')),
                        'latitude': convert_to_decimal(replace_placeholder(standard_fields.get('Latitude'))),
                        'longitude': convert_to_decimal(replace_placeholder(standard_fields.get('Longitude'))),
                        'year_built': convert_to_decimal(replace_placeholder(standard_fields.get('YearBuilt'))),
                        'bedrooms': convert_to_decimal(replace_placeholder(standard_fields.get('BedsTotal'))),
                        'baths_full': convert_to_decimal(replace_placeholder(standard_fields.get('BathsFull'))),
                        'baths_half': convert_to_decimal(replace_placeholder(standard_fields.get('BathsHalf'))),
                        'baths_three_quarter': convert_to_decimal(replace_placeholder(standard_fields.get('BathsThreeQuarter'))),
                        'building_area_total': convert_to_decimal(replace_placeholder(standard_fields.get('BuildingAreaTotal'))),
                        'public_remarks': replace_placeholder(standard_fields.get('PublicRemarks')),
                        'private_remarks': replace_placeholder(standard_fields.get('PrivateRemarks')),
                        'property_subtype': replace_placeholder(standard_fields.get('PropertySubType')),
                    }
                )
                
            self.stdout.write(self.style.SUCCESS('Successfully fetched and updated properties.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))
