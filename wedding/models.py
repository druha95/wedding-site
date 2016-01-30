#!encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
from django_countries import countries


class Rsvp(models.Model):

    EVENTS_CHOICES = (
        ("sunset_cruise", _("Sunset cruise, 3 PM, Sunday, Feb 14")),
        ("dinner_1", _("Dinner | 7 PM, Sunday, Feb 14")),
        ("beach_wedding", _("Beach wedding, 4 PM, Monday, Feb 15")),
        ("lunch_water", _("Lunch and water activities, 1 PM, Tuesday, Feb 16")),
        ("dinner_2", _("Dinner | 7 PM, Tuesday, Feb 16")),
        ("church_wedding", _("Church wedding, 1 PM, Friday, Feb 19")),
        ("dimsum_brunch", _("Dimsum brunch, 12 noon, Saturday, Feb 20")),
    )

    DIETARY_CHOICES = (
        ("gluten_free", _("Gluten Free")),
        ("halal", _("Halal")),
        ("kosher", _("Kosher")),
        ("pescatarian", _("Pescatarian")),
        ("vegan", _("Vegan")),
        ("vegetarian", _("Vegetarian")),
    )

    NUMBER_OF_GUESTS_CHOICES = [(i, i) for i in range(1, 7)]

    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=50)
    rsvp = models.BooleanField(_("Rsvp"), default=True)
    events = MultiSelectField(
        _("Events attended"), choices=EVENTS_CHOICES, null=True, blank=True)
    manila_flight_into = models.CharField(
        _("Manila arrival flight number (into Manila)"), max_length=20,
        null=True, blank=True)
    manila_date_into = models.DateTimeField(
        _("Manila arrival date and time"), auto_now=False, null=True, blank=True)
    manila_flight_out = models.CharField(
        _("Departure flight number (out of Manila)"), max_length=50, null=True,
        blank=True)
    manila_date_out = models.DateTimeField(
        _("Manila departure date and time"), auto_now=False, null=True, blank=True)
    manila_staying = models.CharField(
        _("Staying in Manila"), max_length=50, choices=EVENTS_CHOICES,
        null=True, blank=True)
    manila_staying_other = models.TextField(
        _("Other..."), max_length=200, null=True, blank=True)
    boracay_flight_into = models.CharField(
        _("Boracay arrival flight number (into Boracay)"), max_length=20,
        null=True, blank=True)
    boracay_date_into = models.DateTimeField(
        _("Boracay arrival date and time"), auto_now=False, null=True, blank=True)
    boracay_flight_out = models.CharField(
        _("Departure flight number (out of Boracay)"), max_length=50, null=True,
        blank=True)
    boracay_date_out = models.DateTimeField(
        _("Boracay departure date and time"), auto_now=False, null=True, blank=True)
    boracay_staying = models.CharField(
        _("Staying in Boracay"), max_length=50, choices=EVENTS_CHOICES,
        null=True, blank=True)
    boracay_staying_other = models.TextField(
        _("Other..."), max_length=200, null=True, blank=True)
    dietary_restrictions = models.CharField(
        _("Your dietary restrictions"), max_length=50, choices=DIETARY_CHOICES,
        null=True, blank=True)
    number_of_guests = models.PositiveIntegerField(
        _("No. of guests"), null=True, blank=True, choices=NUMBER_OF_GUESTS_CHOICES)
    guests_name_1 = models.CharField(_("Guest's name"), blank=True, max_length=50)
    guests_email_1 = models.EmailField(_("Guest's email"), blank=True, max_length=50)
    guests_dietary_restrictions_1 = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True, blank=True)
    guests_name_2 = models.CharField(_("Guest's name"), blank=True, max_length=50)
    guests_email_2 = models.EmailField(_("Guest's email"), blank=True, max_length=50)
    guests_dietary_restrictions_2 = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True, blank=True)
    guests_name_3 = models.CharField(_("Guest's name"), blank=True, max_length=50)
    guests_email_3 = models.EmailField(_("Guest's email"), blank=True, max_length=50)
    guests_dietary_restrictions_3 = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True, blank=True)
    guests_name_4 = models.CharField(_("Guest's name"), blank=True, max_length=50)
    guests_email_4 = models.EmailField(_("Guest's email"), blank=True, max_length=50)
    guests_dietary_restrictions_4 = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True, blank=True)
    guests_name_5 = models.CharField(_("Guest's name"), blank=True, max_length=50)
    guests_email_5 = models.EmailField(_("Guest's email"), blank=True, max_length=50)
    guests_dietary_restrictions_5 = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True, blank=True)
    additional_comment = models.TextField(
        _("Anything else"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("RSVP")
        verbose_name_plural = _("RSVP")

    def __str__(self):
        return self.name
