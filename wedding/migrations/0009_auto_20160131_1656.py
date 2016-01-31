# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0008_auto_20160130_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='boracay_staying',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Staying in Boracay', choices=[(b'asya', 'Asya (wedding venue)'), (b'discovery_shores', 'Discovery Shores'), (b'villa_caemilla', 'Villa Caemilla'), (b'boracay_other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='manila_staying',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Staying in Manila', choices=[(b'holiday_inn', 'Holiday Inn'), (b'manila_peninsula', 'Manila Peninsula'), (b'shangri_la', 'Makati Shangri-la (wedding venue)'), (b'luxe_residences', 'The Luxe Residences'), (b'manila_other', 'Other')]),
        ),
    ]
