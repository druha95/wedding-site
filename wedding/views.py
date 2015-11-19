from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from wedding.forms import SubmitRsvpForm
from wedding.models import Rsvp


class RsvpCreateView(CreateView):
    """Create View for Reservation"""
    model = Rsvp
    template_name = 'pages/submit_rsvp.html'
    form_class = SubmitRsvpForm

    # def get_success_url(self):
    #     return self.object.working_machine.get_absolute_url()

submit_rsvp = RsvpCreateView.as_view()
