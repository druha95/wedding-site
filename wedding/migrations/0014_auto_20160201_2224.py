# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0013_auto_20160131_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='Email', blank=True),
        ),
    ]
