# Generated by Django 3.1.5 on 2021-07-25 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddHotelStep1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('short_description', models.TextField(max_length=250)),
                ('long_description', models.TextField(max_length=2000)),
                ('star', models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5, max_length=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('street_address', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=100)),
                ('post_code', models.IntegerField(null=True)),
                ('picture', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/%Y/%m/%d/')),
                ('hotel_view', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_view', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True)),
                ('short_description', models.TextField(max_length=250)),
                ('long_description', models.TextField(max_length=2000, null=True)),
                ('picture', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddHotelStep2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('alternative_contact_mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('owner', models.TextField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('hotel_type', models.TextField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Twin', 'Twin'), ('Family', 'Family'), ('Studio', 'Studio')], max_length=10)),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.addhotelstep1')),
            ],
        ),
    ]
