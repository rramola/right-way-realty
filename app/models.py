from django.db import models
import requests


class Property(models.Model):
    # Main Fields
    mls_number = models.CharField(max_length=20, unique=True)
    list_price = models.DecimalField(max_digits=12, decimal_places=2)
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
    baths_full = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    baths_half = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    baths_total = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    baths_three_quarter = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    building_area_total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    property_subtype = models.CharField(max_length=100, blank=True, null=True)
    # Additional Fields
    public_remarks = models.TextField(blank=True, null=True)
    private_remarks = models.TextField(blank=True, null=True)

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
