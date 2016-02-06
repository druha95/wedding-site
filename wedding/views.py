#!encoding:utf-8
from django.http import JsonResponse
from django.views.generic import CreateView
from wedding.forms import SubmitRsvpMiniForm, SubmitRsvpForm
from wedding.models import Rsvp


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    """
    # def form_invalid(self, form):
    #     response = super(AjaxableResponseMixin, self).form_invalid(form)
    #     if self.request.is_ajax():
    #         return JsonResponse(form.errors, status=400)
    #     else:
    #         return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        data = {}
        if self.request.is_ajax():
            return JsonResponse(data, status=200)
        else:
            return response


class RsvpCreateView(AjaxableResponseMixin, CreateView):
    """
    Create View for Rsvp
    """
    model = Rsvp
    template_name = 'base.html'
    form_class = SubmitRsvpForm
    success_url = '/'

submit_rsvp = RsvpCreateView.as_view()


class RsvpMiniCreateView(AjaxableResponseMixin, CreateView):
    """
    Create View for Mini Rsvp
    """
    model = Rsvp
    template_name = 'base.html'
    form_class = SubmitRsvpMiniForm
    success_url = '/'

submit_mini_rsvp = RsvpMiniCreateView.as_view()
