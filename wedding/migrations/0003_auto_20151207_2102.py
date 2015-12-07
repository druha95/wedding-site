# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_auto_20151207_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Guest', 'verbose_name_plural': 'Guests'},
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests',
            field=models.ManyToManyField(to='wedding.Guest'),
        ),
    ]
