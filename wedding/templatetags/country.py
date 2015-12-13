from __future__ import unicode_literals
from django import template
from django_countries import countries

register = template.Library()


@register.inclusion_tag('includes/country_field.html', takes_context=True)
def country_field(context):
    context['country_list'] = countries
    return context
