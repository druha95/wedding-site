from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from wedding.models import Rsvp
from bootstrap3_datetime.widgets import DateTimePicker


class SubmitRsvpForm(forms.ModelForm):
    """Class for Reservation submit form"""

    class Meta:
        model = Rsvp
        fields = '__all__'
        # fields = ['working_machine', 'customer_name',
        #           'reservation_start_time', 'reservation_end_time']
        # widgets = {
        #     'reservation_start_time': DateTimePicker(
        #         options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}
        #     ),
        #     'reservation_end_time': DateTimePicker(
        #         options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}
        #     )
        # }

    def save(self, commit=True):
        new_rsvp = super(SubmitRsvpForm, self).save(commit=False)
        name = self.fields['name']
        email = self.fields['email']
        number_of_guests = self.fields['number_of_guests']
        msg = u'Name: {} \nEmail: {}\nNumber of guests: {}' \
            .format(name, email, number_of_guests)
        if int(number_of_guests) > 1:
            subject = u'{} just RSVP\'d with {} guests'\
                .format(name, number_of_guests)
        else:
            subject = u'{} just RSVP\'d with {} guest'\
                .format(name, number_of_guests)
        send_mail(
            subject, msg, 'party@karenmichael.com', ['party@karenmichael.com'])
        if commit:
            new_rsvp.save()
        return new_rsvp
