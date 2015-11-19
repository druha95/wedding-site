from django.contrib import admin
from wedding.models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Rsvp, RsvpAdmin)
