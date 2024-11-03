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
        def replace_placeholder(value):
            if value == '*':
                return None
            return value
        def convert_to_decimal(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

        try:
            # Log in to RETS
            if session.login():
                self.stdout.write(self.style.SUCCESS('Successfully logged in to RETS'))

                system_data = session.get_system_metadata()
                # self.stdout.write(self.style.SUCCESS(f'SYSTEM DATA {system_data}'))
                # Fetch resource metadata
                resources = session.get_resource_metadata(resource='Property')
                # self.stdout.write(self.style.SUCCESS(f'PROPERTY RESOURCE DATA {resources}'))
                # Fetch class metadata for the Property resource
                class_metadata = session.get_class_metadata(resource='Property')
                # self.stdout.write(self.style.SUCCESS(f'PROPERTY METADATA {class_metadata}'))
                # Fetch table metadata for the Residential class
                table_metadata = session.get_table_metadata(resource='Property', resource_class="A")
                # self.stdout.write(self.style.SUCCESS(f'PROPERTY A DATA {table_metadata}'))

                # Define a DMQL query to fetch active property data
                dmql_query = "(LIST_15=Active)"  # Ensure 'A' corresponds to active listings
   
                # Fetch property data using the DMQL query
                properties = list(session.search('Property', resource_class='ResidentialProperty', dmql_query=('*'), standard_names=1))
                properties1 = list(session.search('Property', resource_class='A', dmql_query=('*'), standard_names=0))
                # test1 = []
                # test1.append(properties[0])
                # test1.append(properties[1])
                self.stdout.write(self.style.SUCCESS(f'PROPERTIES {properties[0]}'))
                self.stdout.write(self.style.SUCCESS(f'PROPERTIES {properties1[0]}'))

                # Check if properties were fetched
                if not properties:
                    self.stdout.write(self.style.WARNING('No properties found for the given query'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Found {len(properties)} properties'))

                # Store fetched properties into the database

                # for listing in test1:
                #     try:
                #         # Create or update Property instance
                #         property_obj, created = Property.objects.update_or_create(
                #             mls_number = listing["ListingID"],
                #             defaults={
                #                 'list_price': convert_to_decimal(replace_placeholder(listing.get('ListPrice'))),
                #                 'subdivision_name': replace_placeholder(listing.get('Subdivision')),
                #                 'house_number': replace_placeholder(listing.get('StreetNumber')),
                #                 'street_name': replace_placeholder(listing.get('StreetName')),
                #                 'street_suffix': replace_placeholder(listing.get('StreetSuffix')),
                #                 'city': replace_placeholder(listing.get('City')),
                #                 'state': 'MS',
                #                 'county': replace_placeholder(listing.get('County')),
                #                 'postal_code': replace_placeholder(listing.get('PostalCode')),
                #                 'description': '',
                #                 'latitude': '',
                #                 'longitude': '',
                #                 'year_built': 0,
                #                 'bedrooms': listing.get('Bedrooms',0),
                #                 'baths_full': convert_to_decimal(replace_placeholder(listing.get('BathsFull'))),
                #                 'baths_half': convert_to_decimal(replace_placeholder(listing.get('BathsHalf'))),
                #                 'baths_total': listing.get('BathsTotal', 0),
                #                 'baths_total_integer': 0,
                #                 'baths_three_quarter': 0,
                #                 'building_area_total': 0,
                #                 'car_port_spaces': 0,
                #                 'public_remarks': replace_placeholder(listing.get('PublicRemarks')),
                #                 'private_remarks': replace_placeholder(listing.get('Remarks')),
                #                 'property_subtype': replace_placeholder(listing.get('Style')),
                #                 'property_type': '',
                #                 'appliances': '',
                #                 'building_features': '',
                #                 'carport': '',
                #                 'construction_materials': '',
                #                 'cooling': '',
                #                 'highschool_district': replace_placeholder(listing.get('SchoolDistrict')),
                #                 'interior_features': '',
                #                 'laundry_features': '',
                #                 'levels': '',
                #                 'middle_junior_school_district': replace_placeholder(listing.get('SchoolDistrict')),
                #                 'mls_status': replace_placeholder(listing.get('ListingStatus')),
                #                 'roof': '',
                #                 'sewer': '',
                #                 'water_source': '',
                #                 'days_on_market': 0,
                #                 'electric': replace_placeholder(listing.get('Utilities')),
                #                 'exterior_features': '',
                #                 'fireplace_yes_no': '',
                #                 'fireplace_features': replace_placeholder(listing.get('Fireplaces')),
                #                 'flooring': '',
                #                 'foundation_details': '',
                #                 'garage_spaces': 0,
                #                 'garage_yes_no': '',
                #                 'heating': '',
                #                 'heating_yes_no': '',
                #                 'lot_size_acres': 0,
                #                 'mls_area': replace_placeholder(listing.get('ListingArea')),
                #                 'parking_features': '',
                #                 'patio_porch_features': '',
                #                 'pool_features': '',
                #                 'pool_private_yes_no': '',
                #                 'road_surface_type': '',
                #                 'zoning': replace_placeholder(listing.get('Zoning')),
                #                 'zoning_description': '',
                #                 'address_is_displayed': '',              
                #                 'other_structures': '',
                #                 'property_subtype': '',
                #                 'virtual_tour_url': '',
                #                 'modification_timestamp': replace_placeholder(listing.get('ModificationTimestamp')),
                #                 'original_entry_timestamp': '',
                #                 'price_change_timestamp': '',
                #             }
                #         )
                #         self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} property: {property_obj.mls_number}"))
                #     except Exception as e:
                #         self.stdout.write(self.style.ERROR(f"Error processing property: {e}"))
                        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error logging in or fetching data: {e}"))
