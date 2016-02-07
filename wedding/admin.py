from django.contrib import admin
from wedding.models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'rsvp', 'events', 'manila_flight_into',
        'manila_date_into', 'manila_flight_out',
        'manila_date_out', 'manila_staying', 'manila_staying_other',
        'boracay_flight_into', 'boracay_date_into',
        'boracay_flight_out', 'boracay_date_out',
        'boracay_staying', 'boracay_staying_other', 'dietary_restrictions',
        'number_of_guests', 'guests_name_1', 'guests_email_1',
        'guests_dietary_restrictions_1',
        'guests_dietary_restrictions_1_other',
        'guests_name_2', 'guests_email_2',
        'guests_dietary_restrictions_2',
        'guests_dietary_restrictions_2_other',
        'guests_name_3', 'guests_email_3',
        'guests_dietary_restrictions_3',
        'guests_dietary_restrictions_3_other',
        'guests_name_4', 'guests_email_4',
        'guests_dietary_restrictions_4',
        'guests_dietary_restrictions_4_other',
        'guests_name_5', 'guests_email_5',
        'guests_dietary_restrictions_5',
        'guests_dietary_restrictions_5_other',
        'additional_comment'
    )

admin.site.register(Rsvp, RsvpAdmin)
