# Generated by Django 5.0.7 on 2024-10-19 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mls_number', models.CharField(max_length=20, unique=True)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('subdivision_name', models.CharField(blank=True, max_length=50, null=True)),
                ('house_number', models.CharField(blank=True, max_length=10, null=True)),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('street_suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('year_built', models.IntegerField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('baths_full', models.IntegerField(blank=True, null=True)),
                ('baths_half', models.IntegerField(blank=True, null=True)),
                ('baths_total_integer', models.IntegerField(blank=True, null=True)),
                ('baths_total', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('baths_three_quarter', models.IntegerField(blank=True, null=True)),
                ('building_area_total', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('car_port_spaces', models.CharField(blank=True, null=True)),
                ('property_type', models.CharField(blank=True, max_length=50, null=True)),
                ('public_remarks', models.TextField(blank=True, null=True)),
                ('private_remarks', models.TextField(blank=True, null=True)),
                ('appliances', models.JSONField(blank=True, null=True)),
                ('building_features', models.JSONField(blank=True, null=True)),
                ('carport', models.BooleanField(blank=True, null=True)),
                ('construction_materials', models.JSONField(blank=True, null=True)),
                ('cooling', models.JSONField(blank=True, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('highschool_district', models.CharField(blank=True, max_length=50, null=True)),
                ('interior_features', models.JSONField(blank=True, null=True)),
                ('laundry_features', models.JSONField(blank=True, null=True)),
                ('levels', models.JSONField(blank=True, null=True)),
                ('middle_junior_school_district', models.CharField(blank=True, max_length=50, null=True)),
                ('mls_status', models.CharField(blank=True, max_length=50, null=True)),
                ('roof', models.JSONField(blank=True, null=True)),
                ('sewer', models.JSONField(blank=True, null=True)),
                ('water_source', models.JSONField(blank=True, null=True)),
                ('days_on_market', models.IntegerField(blank=True, null=True)),
                ('electric', models.JSONField(blank=True, null=True)),
                ('exterior_features', models.JSONField(blank=True, null=True)),
                ('fireplace_yes_no', models.BooleanField(blank=True, null=True)),
                ('fireplace_features', models.JSONField(blank=True, null=True)),
                ('flooring', models.JSONField(blank=True, null=True)),
                ('foundation_details', models.JSONField(blank=True, null=True)),
                ('garage_spaces', models.IntegerField(blank=True, null=True)),
                ('garage_yes_no', models.BooleanField(blank=True, null=True)),
                ('heating', models.JSONField(blank=True, null=True)),
                ('heating_yes_no', models.BooleanField(blank=True, null=True)),
                ('lot_size_acres', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('mls_area', models.CharField(blank=True, max_length=50, null=True)),
                ('parking_features', models.JSONField(blank=True, null=True)),
                ('patio_porch_features', models.JSONField(blank=True, null=True)),
                ('pool_features', models.JSONField(blank=True, null=True)),
                ('pool_private_yes_no', models.BooleanField(blank=True, null=True)),
                ('road_surface_type', models.JSONField(blank=True, null=True)),
                ('zoning', models.CharField(blank=True, max_length=50, null=True)),
                ('zoning_description', models.CharField(blank=True, max_length=50, null=True)),
                ('address_is_displayed', models.BooleanField(blank=True, null=True)),
                ('other_structures', models.JSONField(blank=True, null=True)),
                ('property_subtype', models.CharField(blank=True, max_length=50, null=True)),
                ('virtual_tour_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('available_from', models.DateField()),
                ('school', models.TextField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('baths', models.IntegerField(blank=True, null=True)),
                ('deposit_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('fenced_yard', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('media_id', models.CharField(blank=True, max_length=50, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.property')),
            ],
        ),
        migrations.CreateModel(
            name='RentalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rental_images/')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.rental')),
            ],
        ),
    ]
