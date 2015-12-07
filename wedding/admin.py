from django.contrib import admin
from wedding.models import Guest, Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'rsvp', 'events', 'manila_flight_into',
        'manila_date_into', 'manila_time_into', 'manila_flight_out',
        'manila_date_out', 'manila_time_out', 'manila_staying',
        'boracay_flight_into', 'boracay_date_into', 'boracay_time_into',
        'boracay_flight_out', 'boracay_date_out', 'boracay_time_out',
        'boracay_staying', 'number_of_guests'
    )

admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Guest)
