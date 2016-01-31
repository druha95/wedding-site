# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0010_auto_20160131_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='dietary_restrictions_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
    ]
