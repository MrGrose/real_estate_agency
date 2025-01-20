# Generated by Django 2.2.24 on 2025-01-20 17:48

from django.db import migrations


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year and flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()


def reverse_fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building, reverse_fill_new_building),
    ]