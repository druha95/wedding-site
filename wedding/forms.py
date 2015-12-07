#!encoding:utf-8
from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from wedding.models import Rsvp
from bootstrap3_datetime.widgets import DateTimePicker


class SubmitRsvpMiniForm(forms.ModelForm):
    """Class for Rsvp submit form (user selected NO or nothing)"""

    class Meta:
        model = Rsvp
        fields = ['name', 'email', ]

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpMiniForm, self).save(commit=False)
        new_rsvp.rsvp = False
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject_party = u'{} can\'t make it to the Philippines :('.format(name)
        subject_guest = u'Sad that we can\'t celebrate with you :('
        body_party = u'{} can\'t make it to the Philippines :('.format(name)
        body_guest = u':(\n\nWe\'re sad that we can\'t celebrate with you. We hope to find another occasion for us to celebrate with you.\n\nLove,\nKaren + Michael'
        # send mail to party@karenmichael.com
        send_mail(
            subject_party, body_party, 'party@karenmichael.com',
            ['cherkaev.oleg@gmail.com'])
        # send mail to guest email
        send_mail(
            subject_guest, body_guest, 'party@karenmichael.com',
            [str(email)])
        if commit:
            new_rsvp.save()
        return new_rsvp


class SubmitRsvpForm(forms.ModelForm):
    """Class for Rsvp submit form"""
    manila_date_into = forms.DateField(
        widget=DateTimePicker(
            options={"format": "MM-DD-YYYY", "pickTime": False}),
        input_formats=['%m-%d-%Y', ])
    manila_time_into = forms.TimeField(
        widget=DateTimePicker(
            options={"format": "HH:mm", "pickSeconds": False,
                     "pickDate": False}),
        input_formats=['%H:%M', ])
    manila_date_out = forms.DateField(
        widget=DateTimePicker(
            options={"format": "MM-DD-YYYY", "pickTime": False}),
        input_formats=['%m-%d-%Y', ])
    manila_time_out = forms.TimeField(
        widget=DateTimePicker(
            options={"format": "HH:mm", "pickSeconds": False,
                     "pickDate": False}),
        input_formats=['%H:%M', ])
    boracay_date_into = forms.DateField(
        widget=DateTimePicker(
            options={"format": "MM-DD-YYYY", "pickTime": False}),
        input_formats=['%m-%d-%Y', ])
    boracay_time_into = forms.TimeField(
        widget=DateTimePicker(
            options={"format": "HH:mm", "pickSeconds": False,
                     "pickDate": False}),
        input_formats=['%H:%M', ])
    boracay_date_out = forms.DateField(
        widget=DateTimePicker(
            options={"format": "MM-DD-YYYY", "pickTime": False}),
        input_formats=['%m-%d-%Y', ])
    boracay_time_out = forms.TimeField(
        widget=DateTimePicker(
            options={"format": "HH:mm", "pickSeconds": False,
                     "pickDate": False}),
        input_formats=['%H:%M', ])

    class Meta:
        model = Rsvp
        exclude = ['rsvp', 'guests', ]

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpForm, self).save(commit=False)
        new_rsvp.rsvp = True
        post_data = self.cleaned_data
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        number_of_guests = self.cleaned_data['number_of_guests']
        if int(number_of_guests) == 0 or int(number_of_guests) == 1:
            post_data['guests_template'] = u'guest'
        else:
            post_data['guests_template'] = u'guests'
        subject_party = u'{} will come to the Philippines with {} {}'\
            .format(name, number_of_guests, post_data['guests_template'])
        subject_guest = u'Woohoo! Can\'t wait to celebrate with you :)'
        # send mail to party@karenmichael.com
        body_party_html = render_to_string(
            'mail/body_party.html', {'data': post_data})
        body_party = render_to_string(
            'mail/body_party.html', {'data': post_data})
        send_mail(
            subject_party, body_party, 'party@karenmichael.com',
            ['cherkaev.oleg@gmail.com'], html_message=body_party_html)
        # send mail to guest email
        body_guest_html = render_to_string(
            'mail/body_guest.html', {'data': post_data})
        body_guest = render_to_string(
            'mail/body_guest.html', {'data': post_data})
        send_mail(
            subject_guest, body_guest, 'party@karenmichael.com',
            [str(email)], html_message=body_guest_html)
        if commit:
            new_rsvp.save()
        return new_rsvp
