from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.


# def hello(request):
#     return HttpResponse('Contact page')
#

class ContactCreateView(CreateView):
    template_name = 'contact/contact_us.html'
    model = Contact
    form_class = ContactForm
    # fields = __all__
    success_url = reverse_lazy('home-page')