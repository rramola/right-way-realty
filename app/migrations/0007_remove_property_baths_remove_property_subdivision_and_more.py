# Generated by Django 5.0.7 on 2024-08-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_property_baths_alter_property_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="baths",
        ),
        migrations.RemoveField(
            model_name="property",
            name="subdivision",
        ),
        migrations.AddField(
            model_name="property",
            name="baths_full",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=3, null=True
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="baths_half",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=3, null=True
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="baths_three_quarter",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=3, null=True
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="building_area_total",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="postal_code",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="private_remarks",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="property",
            name="public_remarks",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="property",
            name="state",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="street_suffix",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="year_built",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="bedrooms",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="house_number",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="list_price",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name="property",
            name="mls_number",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="street_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
