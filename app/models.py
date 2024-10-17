from django.db import models
import requests


class Property(models.Model):
    # Main Fields
    mls_number = models.CharField(max_length=20, unique=True)
    list_price = models.DecimalField(max_digits=12, decimal_places=2)
    subdivision_name = models.CharField(max_length=50, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    street_name = models.CharField(max_length=100, blank=True, null=True)
    street_suffix = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    baths_full = models.IntegerField(null=True, blank=True)
    baths_half = models.IntegerField(null=True, blank=True)
    baths_total_integer = models.IntegerField(null=True, blank=True)
    baths_total = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    baths_three_quarter = models.IntegerField(null=True, blank=True)
    building_area_total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    car_port_spaces = models.CharField(null=True, blank=True)
    property_subtype = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=50, blank=True, null=True)
    # Additional Fields
    public_remarks = models.TextField(blank=True, null=True)
    private_remarks = models.TextField(blank=True, null=True)
    appliances = models.JSONField(blank=True, null=True)
    building_features = models.JSONField(blank=True, null=True)
    carport = models.BooleanField(blank=True, null=True)
    construction_materials = models.JSONField(blank=True, null=True)
    cooling = models.JSONField(blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    highschool_district = models.CharField(max_length=50, blank=True, null=True)
    interior_features = models.JSONField(blank=True, null=True)
    laundry_features = models.JSONField(blank=True, null=True)
    levels = models.JSONField(blank=True, null=True)
    middle_junior_school_district = models.CharField(max_length=50, blank=True, null=True)
    mls_status = models.CharField(max_length=50, blank=True, null=True)
    roof = models.JSONField(blank=True, null=True)
    sewer = models.JSONField(blank=True, null=True)
    water_source = models.JSONField(blank=True, null=True)
    days_on_market = models.IntegerField(null=True, blank=True)
    electric = models.JSONField(blank=True, null=True)
    exterior_features = models.JSONField(blank=True, null=True)
    fireplace_yes_no = models.BooleanField(blank=True, null=True)
    fireplace_features = models.JSONField(blank=True, null=True)
    flooring = models.JSONField(blank=True, null=True)
    foundation_details = models.JSONField(blank=True, null=True)
    garage_spaces = models.IntegerField(null=True, blank=True)
    garage_yes_no = models.BooleanField(blank=True, null=True)
    heating = models.JSONField(blank=True, null=True)
    heating_yes_no = models.BooleanField(blank=True, null=True)
    lot_size_acres = models.IntegerField(blank=True, null=True)
    parking_features = models.JSONField(blank=True, null=True)
    patio_porch_features = models.JSONField(blank=True, null=True)
    pool_features = models.JSONField(blank=True, null=True)
    pool_private_yes_no = models.BooleanField(blank=True, null=True)
    road_surface_type = models.JSONField(blank=True, null=True)
    zoning = models.CharField(max_length=50, blank=True, null=True)
    zoning_description = models.CharField(max_length=50, blank=True, null=True)

    

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            address = f"{self.house_number} {self.street_name}, {self.city}"
            self.latitude, self.longitude = self.geocode_address(address)
        super(Property, self).save(*args, **kwargs)

    def geocode_address(self, address):
        api_key = "AIzaSyDvMHU4swcbaypo_PBbgpywoXo5Xa-NSlU"
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
        response = requests.get(url)
        geocode_result = response.json()
        if geocode_result["status"] == "OK":
            location = geocode_result["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            return None, None

    def __str__(self):
        return f'{self.street_name} {self.street_suffix}, {self.city}, {self.state} {self.postal_code}'


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name="images", on_delete=models.CASCADE
    )
    media_id = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    media_id = models.CharField(max_length=50, blank=True, null=True)
   
    # image = models.ImageField(upload_to="property_images/")


    def __str__(self):
        return f"Image for {self.listing.mls_number}"
