# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name="Guest's name")),
                ('email', models.EmailField(max_length=50, verbose_name="Guest's email")),
                ('shoe_size', models.PositiveIntegerField(null=True, verbose_name='Guest\u2019s shoe size', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('dietary_restrictions', models.CharField(max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'sunset_cruise', 'Sunset cruise, 3 PM, Sunday, Feb 14'), (b'beach_wedding', 'Beach wedding, 4 PM, Monday, Feb 15'), (b'chill_beach', 'Chill on the beach, 1 PM, Tuesday, Feb 16'), (b'church_wedding', 'Church wedding, 1 PM, Friday, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch, 12 noon, Saturday, Feb 20')])),
            ],
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guest_dietary_restrictions',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guest_email',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guest_name',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='guest_shoe_size',
        ),
    ]
