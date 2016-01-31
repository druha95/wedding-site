# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0012_auto_20160131_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='dietary_restrictions',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Your dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests_dietary_restrictions_5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guest\u2019s dietary restrictions', choices=[(b'gluten_free', 'Gluten Free'), (b'halal', 'Halal'), (b'kosher', 'Kosher'), (b'pescatarian', 'Pescatarian'), (b'vegan', 'Vegan'), (b'vegetarian', 'Vegetarian'), (b'other', 'Other')]),
        ),
    ]
