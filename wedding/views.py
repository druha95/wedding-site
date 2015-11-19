from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from form.models import Rsvp

# Create your views here.
# def submit_rsvp(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         number_of_guests = request.POST.get('number_of_guests', '')

#         new_rsvp = Rsvp(name=name, email=email, number_of_guests=number_of_guests)
#         new_rsvp.save()
#         msg = u'Name: {} \nEmail: {}\nNumber of guests: {}' \
#             .format(name, email, number_of_guests)
#         if int(number_of_guests) > 1:
#             subject = u'{} just RSVP\'d with {} guests'.format(name, number_of_guests)
#         else:
#             subject = u'{} just RSVP\'d with {} guest'.format(name, number_of_guests)
#         send_mail(subject, msg, 'party@karenmichael.com', ['party@karenmichael.com'])
#     return HttpResponse('OK')