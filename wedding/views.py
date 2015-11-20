#!encoding:utf-8
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from wedding.forms import SubmitRsvpMiniForm, SubmitRsvpForm
from wedding.models import Rsvp


class RsvpCreateView(CreateView):
    """Create View for Rsvp"""
    model = Rsvp
    template_name = 'pages/submit_rsvp.html'
    form_class = SubmitRsvpForm
    success_url = '/'

submit_rsvp = RsvpCreateView.as_view()


class RsvpMiniCreateView(CreateView):
    """Create View for Rsvp"""
    model = Rsvp
    template_name = 'pages/submit_rsvp.html'
    form_class = SubmitRsvpMiniForm
    success_url = '/'

submit_mini_rsvp = RsvpMiniCreateView.as_view()
