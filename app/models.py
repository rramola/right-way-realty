from django.db import models

import requests


class Property(models.Model):
    mls_number = models.CharField(max_length=100, unique=True)
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    house_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    baths = models.DecimalField(max_digits=2, decimal_places=1)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

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
        return f"{self.mls_number} - {self.street_name}, {self.city}"


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return f"Image for {self.property.mls_number}"
