from django.db import models

class Property(models.Model):
    mls_number = models.CharField(max_length=100, unique=True, default='MLS0000')
    list_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    house_number = models.CharField(max_length=10, default='0')
    street_name = models.CharField(max_length=100, default='Unknown Street')
    bedrooms = models.IntegerField(default=0)
    baths = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    subdivision = models.CharField(max_length=100, default='Unknown Subdivision')
    city = models.CharField(max_length=100, default='Unknown City')
    description = models.TextField(default='No description available.')

    def __str__(self):
        return self.mls_number

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.URLField(max_length=200)

    def __str__(self):
        return f"Image for {self.property.mls_number}"
