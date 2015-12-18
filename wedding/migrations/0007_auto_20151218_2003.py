# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_auto_20151218_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_shoe_size_1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_shoe_size_2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_shoe_size_3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_shoe_size_4',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_shoe_size_5',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
