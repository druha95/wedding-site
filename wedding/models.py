#!encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField


class Rsvp(models.Model):

    EVENTS_CHOICES = (
        ("sunset_cruise", _("Sunset cruise, 3 PM, Sunday, Feb 14")),
        ("beach_wedding", _("Beach wedding, 4 PM, Monday, Feb 15")),
        ("chill_beach", _("Chill on the beach, 1 PM, Tuesday, Feb 16")),
        ("church_wedding", _("Church wedding, 1 PM, Friday, Feb 19")),
        ("dimsum_brunch", _("Dimsum brunch, 12 noon, Saturday, Feb 20")),
    )

    SHOE_SIZE_CHOICES = (
        (1, _("1")),
        (2, _("2")),
        (3, _("3")),
        (4, _("4")),
        (5, _("5")),
    )

    DIETARY_CHOICES = (
        ("sunset_cruise", _("Sunset cruise, 3 PM, Sunday, Feb 14")),
        ("beach_wedding", _("Beach wedding, 4 PM, Monday, Feb 15")),
        ("chill_beach", _("Chill on the beach, 1 PM, Tuesday, Feb 16")),
        ("church_wedding", _("Church wedding, 1 PM, Friday, Feb 19")),
        ("dimsum_brunch", _("Dimsum brunch, 12 noon, Saturday, Feb 20")),
    )

    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=50)
    rsvp = models.BooleanField(_("Rsvp"), default=True)
    street_address = models.CharField(
        _("Street address"), max_length=50, null=True)
    street_address_cont = models.CharField(
        _("Street address (continued)"), max_length=50, null=True)
    city = models.CharField(_("City"), max_length=50, null=True)
    state = models.CharField(
        _("State / Province / Region"), max_length=50, null=True)
    zip_code = models.PositiveIntegerField(_("Zip / Postal code"), null=True)
    country = models.CharField(_("Country"), max_length=50, null=True)
    events = MultiSelectField(
        _("Events attended"), choices=EVENTS_CHOICES, null=True)
    manila_flight_into = models.CharField(
        _("Manila arrival flight number (into Manila)"), max_length=20,
        null=True)
    manila_date_into = models.DateField(
        _("Manila arrival date"), auto_now=False, null=True)
    manila_time_into = models.DateTimeField(
        _("Manila arrival time"), auto_now=False, null=True)
    manila_flight_out = models.CharField(
        _("Departure flight number (out of Manila)"), max_length=50, null=True)
    manila_date_out = models.DateField(
        _("Manila departure date"), auto_now=False, null=True)
    manila_time_out = models.DateTimeField(
        _("Manila departure time"), auto_now=False, null=True)
    manila_staying = models.CharField(
        _("Staying in Manila"), max_length=50, choices=EVENTS_CHOICES,
        null=True)
    boracay_flight_into = models.CharField(
        _("Boracay arrival flight number (into Boracay)"), max_length=20,
        null=True)
    boracay_date_into = models.DateField(
        _("Boracay arrival date"), auto_now=False, null=True)
    boracay_time_into = models.DateTimeField(
        _("Boracay arrival time"), auto_now=False, null=True)
    boracay_flight_out = models.CharField(
        _("Departure flight number (out of Boracay)"), max_length=50, null=True)
    boracay_date_out = models.DateField(
        _("Boracay departure date"), auto_now=False, null=True)
    boracay_time_out = models.DateTimeField(
        _("Boracay departure time"), auto_now=False, null=True)
    boracay_staying = models.CharField(
        _("Staying in Boracay"), max_length=50, choices=EVENTS_CHOICES,
        null=True)
    shoe_size = models.PositiveIntegerField(
        _("Your shoe size"), choices=SHOE_SIZE_CHOICES, null=True)
    dietary_restrictions = models.CharField(
        _("Your dietary restrictions"), max_length=50, choices=DIETARY_CHOICES,
        null=True)
    number_of_guests = models.PositiveIntegerField(
        _("No. of guests"), null=True)
    guest_name = models.CharField(_("Guest’s name"), max_length=50, null=True)
    guest_email = models.EmailField(
        _("Guest’s email"), max_length=50, null=True)
    guest_shoe_size = models.PositiveIntegerField(
        _("Guest’s shoe size"), choices=SHOE_SIZE_CHOICES, null=True)
    guest_dietary_restrictions = models.CharField(
        _("Guest’s dietary restrictions"), max_length=50,
        choices=DIETARY_CHOICES, null=True)
    additional_comment = models.TextField(
        _("Anything else"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("RSVP")
        verbose_name_plural = _("RSVP")

    def __str__(self):
        return self.name
