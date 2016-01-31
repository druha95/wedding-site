# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0011_rsvp_dietary_restrictions_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_1_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_2_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_3_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_4_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guests_dietary_restrictions_5_other',
            field=models.TextField(max_length=200, null=True, verbose_name='Other...', blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='number_of_guests',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='No. of guests', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
