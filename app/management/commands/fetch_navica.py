import requests
from django.core.management.base import BaseCommand
from app.navica import NavicaAPI
from app.models import Property, PropertyImage
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
            data = listing_data['bundle']
            fetched_ids = {listing["ListingId"] for listing in data}


            for listing in data:
                images = listing['Media']

                property_obj, created = Property.objects.update_or_create(
                    mls_number = listing["ListingId"],
                      defaults={
                        'list_price': convert_to_decimal(replace_placeholder(listing.get('ListPrice'))),
                        'subdivision_name': replace_placeholder(listing.get('SubdivisionName')),
                        'house_number': replace_placeholder(listing.get('StreetNumber')),
                        'street_name': replace_placeholder(listing.get('StreetName')),
                        'street_suffix': replace_placeholder(listing.get('StreetSuffix')),
                        'city': replace_placeholder(listing.get('City')),
                        'state': replace_placeholder(listing.get('StateOrProvince')),
                        'county': replace_placeholder(listing.get('CountyOrParish')),
                        'postal_code': replace_placeholder(listing.get('PostalCode')),
                        'description': replace_placeholder(listing.get('PublicRemarks')),
                        'latitude': convert_to_decimal(replace_placeholder(listing.get('Latitude'))),
                        'longitude': convert_to_decimal(replace_placeholder(listing.get('Longitude'))),
                        'year_built': convert_to_decimal(replace_placeholder(listing.get('YearBuilt'))),
                        'bedrooms': listing.get('BedroomsTotal',0),
                        'baths_full': convert_to_decimal(replace_placeholder(listing.get('BathroomsFull'))),
                        'baths_half': convert_to_decimal(replace_placeholder(listing.get('BathroomsHalf'))),
                        'baths_total': listing.get('BathroomsTotalDecimal', 0),
                        'baths_total_integer': listing.get('BathroomsTotalInteger', 0),
                        'baths_three_quarter': convert_to_decimal(replace_placeholder(listing.get('BathsThreeQuarter'))),
                        'building_area_total': convert_to_decimal(replace_placeholder(listing.get('BuildingAreaTotal'))),
                        'car_port_spaces': listing.get('CarportSpaces'),
                        'public_remarks': replace_placeholder(listing.get('PublicRemarks')),
                        'private_remarks': replace_placeholder(listing.get('PrivateRemarks')),
                        'property_subtype': replace_placeholder(listing.get('PropertySubType')),
                        'property_type': replace_placeholder(listing.get('PropertyType')),
                        'appliances': replace_placeholder(listing.get('Appliances')),
                        'building_features': replace_placeholder(listing.get('BuildingFeatures')),
                        'carport': replace_placeholder(listing.get('CarportYN')),
                        'construction_materials': replace_placeholder(listing.get('ConstructionMaterials')),
                        'cooling': replace_placeholder(listing.get('Cooling')),
                        'highschool_district': replace_placeholder(listing.get('HighSchoolDistrict')),
                        'interior_features': replace_placeholder(listing.get('InteriorFeatures')),
                        'laundry_features': replace_placeholder(listing.get('InteriorFeatures')),
                        'levels': replace_placeholder(listing.get('InteriorFeatures')),
                        'middle_junior_school_district': replace_placeholder(listing.get('MiddleOrJuniorSchoolDistrict')),
                        'mls_status': replace_placeholder(listing.get('MlsStatus')),
                        'roof': replace_placeholder(listing.get('Roof')),
                        'sewer': replace_placeholder(listing.get('Sewer')),
                        'water_source': replace_placeholder(listing.get('WaterSource')),
                        'days_on_market': replace_placeholder(listing.get('DaysOnMarket')),
                        'electric': replace_placeholder(listing.get('Electric')),
                        'exterior_features': replace_placeholder(listing.get('ExteriorFeatures')),
                        'fireplace_yes_no': replace_placeholder(listing.get('FireplaceYN')),
                        'fireplace_features': replace_placeholder(listing.get('FireplaceFeatures')),
                        'flooring': replace_placeholder(listing.get('Flooring')),
                        'foundation_details': replace_placeholder(listing.get('FoundationDetails')),
                        'garage_spaces': replace_placeholder(listing.get('GarageSpaces')),
                        'garage_yes_no': replace_placeholder(listing.get('GarageYN')),
                        'heating': replace_placeholder(listing.get('Heating')),
                        'heating_yes_no': replace_placeholder(listing.get('HeatingYN')),
                        'lot_size_acres': replace_placeholder(listing.get('LotSizeAcres')),
                        'mls_area': replace_placeholder(listing.get('MLSAreaMajor')),
                        'parking_features': replace_placeholder(listing.get('ParkingFeatures')),
                        'patio_porch_features': replace_placeholder(listing.get('PatioAndPorchFeatures')),
                        'pool_features': replace_placeholder(listing.get('PoolFeatures')),
                        'pool_private_yes_no': replace_placeholder(listing.get('PoolPrivateYN')),
                        'road_surface_type': replace_placeholder(listing.get('RoadSurfaceType')),
                        'zoning': replace_placeholder(listing.get('Zoning')),
                        'zoning_description': replace_placeholder(listing.get('ZoningDescription')),
                        'address_is_displayed': replace_placeholder(listing.get('InternetAddressDisplayYN')),              
                        'other_structures': replace_placeholder(listing.get('OtherStructures')),
                        'price_change_timestamp': replace_placeholder(listing.get('PriceChangeTimestamp')),
                        'property_subtype': replace_placeholder(listing.get('PropertySubType')),
                        'virtual_tour_url': replace_placeholder(listing.get('VirtualTourURLUnbranded')),
                    }
                )

                for image in images:
                    PropertyImage.objects.update_or_create(
                    property=property_obj,
                    media_id=replace_placeholder(image.get('MediaObjectID')),
                    defaults={
                    'url': replace_placeholder(image.get('MediaURL')),
                    'category': replace_placeholder(image.get('MediaCategory')),
                    }
                )
                    
            existing_properties = set(Property.objects.values_list('mls_number', flat=True))
            properties_to_delete = existing_properties - fetched_ids

            if properties_to_delete:
                Property.objects.filter(mls_number__in=properties_to_delete).delete()
                PropertyImage.objects.filter(property__mls_number__in=properties_to_delete).delete()
                self.stdout.write(self.style.SUCCESS(f'Deleted {len(properties_to_delete)} properties from the database.'))


            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))