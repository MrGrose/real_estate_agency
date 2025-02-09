# Generated by Django 2.2.24 on 2025-02-01 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_normalize_phone_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
