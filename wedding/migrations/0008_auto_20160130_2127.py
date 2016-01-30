# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20151218_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='boracay_time_into',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='boracay_time_out',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='city',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='country',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guests_shoe_size_1',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guests_shoe_size_2',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guests_shoe_size_3',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guests_shoe_size_4',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guests_shoe_size_5',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='manila_time_into',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='manila_time_out',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='shoe_size',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='state',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='street_address_cont',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='boracay_staying_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='manila_staying_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_date_into',
            field=models.DateTimeField(null=True, verbose_name='Boracay arrival date and time', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_date_out',
            field=models.DateTimeField(null=True, verbose_name='Boracay departure date and time', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_flight_into',
            field=models.CharField(max_length=20, null=True, verbose_name='Boracay arrival flight number (into Boracay)', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_flight_out',
            field=models.CharField(max_length=50, null=True, verbose_name='Departure flight number (out of Boracay)', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_staying',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Staying in Boracay', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'dinner_1', 'Dinner | 7 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'lunch_water', 'Lunch and water activities, 1 PM, Tuesday, Feb 16'), (b'dinner_2', 'Dinner | 7 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='dietary_restrictions',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Your dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='events',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=86, null=True, verbose_name='Events attended', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'dinner_1', 'Dinner | 7 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'lunch_water', 'Lunch and water activities, 1 PM, Tuesday, Feb 16'), (b'dinner_2', 'Dinner | 7 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_date_into',
            field=models.DateTimeField(null=True, verbose_name='Manila arrival date and time', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_date_out',
            field=models.DateTimeField(null=True, verbose_name='Manila departure date and time', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_flight_into',
            field=models.CharField(max_length=20, null=True, verbose_name='Manila arrival flight number (into Manila)', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_flight_out',
            field=models.CharField(max_length=50, null=True, verbose_name='Departure flight number (out of Manila)', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_staying',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Staying in Manila', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'dinner_1', 'Dinner | 7 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'lunch_water', 'Lunch and water activities, 1 PM, Tuesday, Feb 16'), (b'dinner_2', 'Dinner | 7 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='number_of_guests',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='No. of guests', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
