# Generated by Django 2.2.24 on 2025-01-28 19:21

from django.db import migrations, models


def populate_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owners = Owner.objects.filter(holder=flat.owner)
        flat.owners.set(owners)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20250128_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners',
            field=models.ManyToManyField(
                to='property.Owner',
                related_name='flats',
                blank=True,
                db_index=True,
            ),
        ),
        migrations.RunPython(populate_owners),
    ]
