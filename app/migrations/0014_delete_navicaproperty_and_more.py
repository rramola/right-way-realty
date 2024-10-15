# Generated by Django 5.0.7 on 2024-10-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_property_baths_total'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NavicaProperty',
        ),
        migrations.RenameField(
            model_name='propertyimage',
            old_name='property',
            new_name='listing',
        ),
        migrations.AddField(
            model_name='propertyimage',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='propertyimage',
            name='media_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='propertyimage',
            name='mls_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='propertyimage',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]