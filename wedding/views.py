#!encoding:utf-8
from django.views.generic import CreateView
from mezzanine.pages.views import page
from wedding.forms import SubmitRsvpMiniForm, SubmitRsvpForm
from wedding.models import Rsvp


class RsvpCreateView(CreateView):
    """
    Create View for Rsvp
    """
    model = Rsvp
    template_name = 'pages/submit_rsvp.html'
    form_class = SubmitRsvpForm
    success_url = '/'

submit_rsvp = RsvpCreateView.as_view()


class RsvpMiniCreateView(CreateView):
    """
    Create View for Mini Rsvp
    """
    model = Rsvp
    template_name = 'pages/submit_rsvp.html'
    form_class = SubmitRsvpMiniForm
    success_url = '/'

submit_mini_rsvp = RsvpMiniCreateView.as_view()


def wedding_page(request, slug, template=u"base.html", extra_context=None):
    """
    Overrides Mezzanine's page view, adding rsvp form in context.
    """
    included_rsvp_form = {}
    included_rsvp_form['submit_rsvp_form'] = SubmitRsvpForm()
    included_rsvp_form['submit_rsvp_mini_form'] = SubmitRsvpMiniForm()
    return page(request, slug, template=u"base.html",
                extra_context=included_rsvp_form)
