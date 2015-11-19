# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('street_address', models.CharField(max_length=50, null=True, verbose_name='Street address')),
                ('street_address_cont', models.CharField(max_length=50, null=True, verbose_name='Street address (continued)')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='State / Province / Region')),
                ('zip_code', models.PositiveIntegerField(null=True, verbose_name='Zip / Postal code')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='Country')),
                ('events', multiselectfield.db.fields.MultiSelectField(max_length=68, null=True, verbose_name='Events attended', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('manila_flight_into', models.CharField(max_length=20, null=True, verbose_name='Manila arrival flight number (into Manila)')),
                ('manila_date_into', models.DateField(null=True, verbose_name='Manila arrival date')),
                ('manila_time_into', models.DateTimeField(null=True, verbose_name='Manila arrival time')),
                ('manila_flight_out', models.CharField(max_length=50, null=True, verbose_name='Departure flight number (out of Manila)')),
                ('manila_date_out', models.DateField(null=True, verbose_name='Manila departure date')),
                ('manila_time_out', models.DateTimeField(null=True, verbose_name='Manila departure time')),
                ('manila_staying', models.CharField(max_length=50, null=True, verbose_name='Staying in Manila', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('boracay_flight_into', models.CharField(max_length=20, null=True, verbose_name='Boracay arrival flight number (into Boracay)')),
                ('boracay_date_into', models.DateField(null=True, verbose_name='Boracay arrival date')),
                ('boracay_time_into', models.DateTimeField(null=True, verbose_name='Boracay arrival time')),
                ('boracay_flight_out', models.CharField(max_length=50, null=True, verbose_name='Departure flight number (out of Boracay)')),
                ('boracay_date_out', models.DateField(null=True, verbose_name='Boracay departure date')),
                ('boracay_time_out', models.DateTimeField(null=True, verbose_name='Boracay departure time')),
                ('boracay', models.CharField(max_length=50, null=True, verbose_name='Staying in Boracay', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('shoe_size', models.PositiveIntegerField(null=True, verbose_name='Your shoe size', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('dietary_restrictions', models.CharField(max_length=50, null=True, verbose_name='Your dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('number_of_guests', models.PositiveIntegerField(verbose_name='No. of guests')),
                ('guest_name', models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s name')),
                ('guest_email', models.EmailField(max_length=50, null=True, verbose_name='Guest\u2019s email')),
                ('guest_shoe_size', models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('guest_dietary_restrictions', models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
                ('additional_comment', models.TextField(max_length=200, null=True, verbose_name='Anything else', blank=True)),
            ],
            options={
                'verbose_name': 'RSVP',
                'verbose_name_plural': 'RSVP',
            },
        ),
    ]
