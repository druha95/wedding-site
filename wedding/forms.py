#!encoding:utf-8
from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from wedding.models import Rsvp
from bootstrap3_datetime.widgets import DateTimePicker


class SubmitRsvpMiniForm(forms.ModelForm):
    """Class for Rsvp submit form (user selected NO)"""

    class Meta:
        model = Rsvp
        fields = ['name', 'email', ]

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpForm, self).save(commit=False)
        self.fields['rsvp'] = False
        name = self.fields['name']
        email = self.fields['email']
        subject_party = u'{} can\'t make it to the Philippines :('.format(name)
        subject_guest = u'Sad that we can\'t celebrate with you :('
        body_party = u'{} can\'t make it to the Philippines :('.format(name)
        body_guest = u':(\n\nWe\'re sad that we can\'t celebrate with you. \
            We hope to find another occasion for us to celebrate with \
            you.\n\nLove,\nKaren + Michael'
        # send mail to party@karenmichael.com
        send_mail(
            subject_party, body_party, 'party@karenmichael.com',
            ['party@karenmichael.com'])
        # send mail to guest email
        send_mail(
            subject_guest, body_guest, 'party@karenmichael.com',
            [str(email)])
        if commit:
            new_rsvp.save()
        return new_rsvp


class SubmitRsvpForm(forms.ModelForm):
    """Class for Rsvp submit form"""

    class Meta:
        model = Rsvp
        exclude = ['rsvp', ]
        # fields = '__all__'
        widgets = {
            'reservation_start_time': DateTimePicker(
                options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}
            ),
            'reservation_end_time': DateTimePicker(
                options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}
            )
        }

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpForm, self).save(commit=False)
        self.fields['rsvp'] = True
        name = self.fields['name']
        email = self.fields['email']
        events = self.fields['events']
        manila_flight_into = self.fields['manila_flight_into']
        manila_date_into = self.fields['manila_date_into']
        manila_time_into = self.fields['manila_time_into']
        manila_flight_out = self.fields['manila_flight_out']
        manila_date_out = self.fields['manila_date_out']
        manila_time_out = self.fields['manila_time_out']
        manila_staying = self.fields['manila_staying']
        boracay_flight_into = self.fields['boracay_flight_into']
        boracay_date_into = self.fields['boracay_date_into']
        boracay_time_into = self.fields['boracay_time_into']
        boracay_flight_out = self.fields['boracay_flight_out']
        boracay_date_out = self.fields['boracay_date_out']
        boracay_time_out = self.fields['boracay_time_out']
        boracay_staying = self.fields['boracay_staying']
        boracay_flight_into = self.fields['boracay_flight_into']
        number_of_guests = self.fields['number_of_guests']
        guest_name = self.fields['guest_name']
        guest_email = self.fields['guest_email']
        subject_guest = u'Woohoo! Can\'t wait to celebrate with you :)'
        body_guest = u'Yay!\n\nThrilled to hear that you can come and \
            celebrate with us. If there\'s any mistake with the \
            information below, email us at party@karenmichael.com.\
            \n\nLove,\nKaren + Michael\n\n\n\
            Which events will you attend?\n\n{}\n\n\
            When do you arrive in Manila?\n\n\
            Arrival flight number: {}\n\
            Arrival date: {}\n\
            Arrival time: {}\n\
            Departure flight number: {}\n\
            Departure date: {}\n\
            Departure time: {}\n\
            Hotel name: {}\n\n\
            When do you arrive in Boracay?\n\n\
            Arrival flight number: {}\n\
            Arrival date: {}\n\
            Arrival time: {}\n\
            Departure flight number: {}\n\
            Departure date: {}\n\
            Departure time: {}\n\
            Hotel name: {}\n\n\
            Any special guests?\n\n\
            Number of guests (excluding you): {}\n'\
            .format(events, manila_flight_into, manila_date_into,
                    manila_time_into, manila_flight_out, manila_date_out,
                    manila_time_out, manila_staying, boracay_flight_into,
                    boracay_date_into, boracay_time_into, boracay_flight_out,
                    boracay_date_out, boracay_date_out, boracay_time_out,
                    boracay_staying, number_of_guests)
        if guest_name:
            guests_name_string = u'Guest\'s name: {}\n'.format(guest_name)
            body_guest = body_guest + guests_name_string
            if guest_email:
                guest_email_string = u'Guest\'s email: {}\n'.format(guest_email)
                body_guest = body_guest + guest_email_string
        if int(number_of_guests) == 0 or int(number_of_guests) == 1:
            guests_template = u'guest'
        else:
            guests_template = u'guests'
        subject_party = u'{} will come to the Philippines with {} {}'\
            .format(name, number_of_guests, guests_template)
        body_party = u'{} will come to the Philippines with {} {}\n\n\n\
            Which events will you attend?\n\n{}\n\n\
            When do you arrive in Manila?\n\n\
            Arrival flight number: {}\n\
            Arrival date: {}\n\
            Arrival time: {}\n\
            Departure flight number: {}\n\
            Departure date: {}\n\
            Departure time: {}\n\
            Hotel name: {}\n\n\
            When do you arrive in Boracay?\n\n\
            Arrival flight number: {}\n\
            Arrival date: {}\n\
            Arrival time: {}\n\
            Departure flight number: {}\n\
            Departure date: {}\n\
            Departure time: {}\n\
            Hotel name: {}\n\n\
            Any special guests?\n\n\
            Number of guests (excluding you): {}\n'\
            .format(name, number_of_guests, guests_template, events,
                    manila_flight_into, manila_date_into, manila_time_into,
                    manila_flight_out, manila_date_out, manila_time_out,
                    manila_staying, boracay_flight_into, boracay_date_into,
                    boracay_time_into, boracay_flight_out, boracay_date_out,
                    boracay_date_out, boracay_time_out, boracay_staying,
                    number_of_guests)
        if guest_name:
            guests_name_string = u'Guest\'s name: {}\n'.format(guest_name)
            body_party = body_party + guests_name_string
            if guest_email:
                guest_email_string = u'Guest\'s email: {}\n'.format(guest_email)
                body_party = body_party + guest_email_string
        # send mail to party@karenmichael.com
        send_mail(
            subject_party, body_party, 'party@karenmichael.com',
            ['party@karenmichael.com'])
        # send mail to guest email
        send_mail(
            subject_guest, body_guest, 'party@karenmichael.com',
            [str(email)])
        if commit:
            new_rsvp.save()
        return new_rsvp
