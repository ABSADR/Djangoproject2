from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateViwe(CreateView):
    template_name = 'Feedback/create-feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('homepage.html')