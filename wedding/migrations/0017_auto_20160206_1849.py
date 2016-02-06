# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0016_auto_20160206_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_flight_into',
            field=models.CharField(max_length=50, null=True, verbose_name='Boracay arrival flight number (into Boracay)', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_flight_into',
            field=models.CharField(max_length=50, null=True, verbose_name='Manila arrival flight number (into Manila)', blank=True),
        ),
    ]
