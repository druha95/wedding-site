# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_auto_20151213_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='guests',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_1',
            field=models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_2',
            field=models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_3',
            field=models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_4',
            field=models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_5',
            field=models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_email_1',
            field=models.EmailField(max_length=50, verbose_name="Guest's email", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_email_2',
            field=models.EmailField(max_length=50, verbose_name="Guest's email", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_email_3',
            field=models.EmailField(max_length=50, verbose_name="Guest's email", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_email_4',
            field=models.EmailField(max_length=50, verbose_name="Guest's email", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_email_5',
            field=models.EmailField(max_length=50, verbose_name="Guest's email", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_name_1',
            field=models.CharField(max_length=50, verbose_name="Guest's name", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_name_2',
            field=models.CharField(max_length=50, verbose_name="Guest's name", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_name_3',
            field=models.CharField(max_length=50, verbose_name="Guest's name", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_name_4',
            field=models.CharField(max_length=50, verbose_name="Guest's name", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_name_5',
            field=models.CharField(max_length=50, verbose_name="Guest's name", blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_shoe_size_1',
            field=models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_shoe_size_2',
            field=models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_shoe_size_3',
            field=models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_shoe_size_4',
            field=models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_shoe_size_5',
            field=models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
