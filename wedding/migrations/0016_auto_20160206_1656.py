# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0015_auto_20160205_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='events',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=116, null=True, verbose_name='Events attended', choices=[(b'sunset_cruise', 'Sunset cruise | 3 PM, Sun, Feb 14'), (b'dinner_1', 'Dinner | 7 PM, Sun, Feb 14'), (b'beach_wedding', 'Beach wedding | 4 PM, Mon, Feb 15'), (b'lunch_water', 'Lunch and water activities, 1 PM, Tue, Feb 16'), (b'dinner_2', 'Dinner | 7 PM, Tue, Feb 16'), (b'dads_birthday', "Dads' birthdays | 7 PM, Thu, Feb 18"), (b'church_wedding', 'Church wedding | 1 PM, Fri, Feb 19'), (b'coctails_dinner', 'Cocktails and dinner | 6 PM, Fri, Feb 19'), (b'dimsum_brunch', 'Dimsum | 12 noon, Sat, Feb 20')]),
        ),
    ]
