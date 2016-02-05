# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0014_auto_20160201_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='events',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=114, null=True, verbose_name='Events attended', choices=[(b'sunset_cruise', 'Sunset cruise | 3 PM, Sun, Feb 14'), (b'dinner_1', 'Dinner | 7 PM, Sun, Feb 14'), (b'beach_wedding', 'Beach wedding | 4 PM, Mon, Feb 15'), (b'lunch_water', 'Lunch and water activities, 1 PM, Tue, Feb 16'), (b'dinner_2', 'Dinner | 7 PM, Tue, Feb 16'), (b'church_wedding', 'Church wedding | 1 PM, Fri, Feb 19'), (b'dimsum_brunch', 'Dimsum brunch | 12 noon, Sat, Feb 20<'), (b'dads_birthday', "Dad's birthdays | 7 PM, Thu, Feb 18"), (b'dimsum_brunch', 'Reception | 7 PM, Fri, Feb 19')]),
        ),
    ]
