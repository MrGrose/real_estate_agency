# Generated by Django 2.2.24 on 2025-01-21 15:45
from django.db import migrations
from phonenumbers import is_valid_number, parse, is_possible_number


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    owners = Flat.objects.all()

    for owner in owners:
        if owner.owners_phone:
            phone_number = owner.owners_phone

            if is_possible_number(parse(phone_number, 'RU')):
                parsed_number = parse(phone_number, 'RU')

                if is_valid_number(parsed_number):
                    owner.owner_pure_phone = parsed_number
                else:
                    owner.owner_pure_phone = None
            else:
                owner.owner_pure_phone = None

            owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20250121_1833'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
