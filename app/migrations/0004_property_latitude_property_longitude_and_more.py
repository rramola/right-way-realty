# Generated by Django 5.0.7 on 2024-08-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_propertyimage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="property",
            name="baths",
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name="property",
            name="bedrooms",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="property",
            name="city",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="property",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="property",
            name="house_number",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="property",
            name="list_price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="property",
            name="mls_number",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="street_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="property",
            name="subdivision",
            field=models.CharField(max_length=255),
        ),
    ]