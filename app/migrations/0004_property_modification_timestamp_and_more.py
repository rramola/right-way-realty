# Generated by Django 5.0.7 on 2024-10-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_property_virtua'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='modification_timestamp',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='original_entry_timestamp',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_change_timestamp',
            field=models.CharField(blank=True, null=True),
        ),
    ]
