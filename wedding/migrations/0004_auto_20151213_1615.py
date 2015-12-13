# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_auto_20151207_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
