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
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        subject_party = u'{} can\'t make it to the Philippines :('.format(name)
        subject_guest = u'Sad that we can\'t celebrate with you :('
        body_party = u'{} can\'t make it to the Philippines :('.format(name)
        body_guest = u':(\n\nWe\'re sad that we can\'t celebrate with you. We hope to find another occasion to post-celebrate with you.\n\nLove,\nKaren + Michael'
        # send mail to party@karenmichael.com
        send_mail(
            subject_party, body_party, 'Karen + Michael <party@karenmichael.com>',
            ['party@karenmichael.com'])
        # send mail to guest email
        if email:
            send_mail(
                subject_guest, body_guest, 'Karen + Michael <party@karenmichael.com>',
                [str(email)])
        if commit:
            new_rsvp.save()
        return new_rsvp


class SubmitRsvpForm(forms.ModelForm):
    """Class for Rsvp submit form"""
    manila_date_into = forms.DateTimeField(
        required=False, localize=True,
        input_formats=['%d %b %y %H:%M'])
    manila_date_out = forms.DateTimeField(
        required=False, localize=True,
        input_formats=['%d %b %y %H:%M'])
    boracay_date_into = forms.DateTimeField(
        required=False, localize=True,
        input_formats=['%d %b %y %H:%M'])
    boracay_date_out = forms.DateTimeField(
        required=False, localize=True,
        input_formats=['%d %b %y %H:%M'])

    class Meta:
        model = Rsvp
        exclude = ['rsvp', ]

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpForm, self).save(commit=False)
        new_rsvp.rsvp = True
        post_data = self.cleaned_data
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        number_of_guests = self.cleaned_data.get('number_of_guests')
        try:
            if int(number_of_guests) == 0 or int(number_of_guests) == 1:
                post_data['guests_template'] = u'guest'
            else:
                post_data['guests_template'] = u'guests'
        except TypeError:
            pass
        try:
            subject_party = u'{} will come to the Philippines with {} {}'\
                .format(name, number_of_guests, post_data['guests_template'])
        except KeyError:
            subject_party = u'{} will come to the Philippines with 0 guests'\
                .format(name)
            pass
        subject_guest = u'Woohoo! Can\'t wait to celebrate with you :)'
        # send mail to party@karenmichael.com
        body_party_html = render_to_string(
            'mail/body_party.html', {'data': post_data})
        body_party = render_to_string(
            'mail/body_party.html', {'data': post_data})
        send_mail(
            subject_party, body_party, 'Karen + Michael <party@karenmichael.com>',
            ['party@karenmichael.com'], html_message=body_party_html)
        # send mail to guest email
        body_guest_html = render_to_string(
            'mail/body_guest.html', {'data': post_data})
        body_guest = render_to_string(
            'mail/body_guest.html', {'data': post_data})
        if email:
            send_mail(
                subject_guest, body_guest, 'Karen + Michael <party@karenmichael.com>',
                [str(email)], html_message=body_guest_html)
        if commit:
            new_rsvp.save()
        return new_rsvp
