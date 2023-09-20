from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(CreateView):
    template_name = 'Feedback/create-feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('home-page')


class FeedbackListView(ListView):
    template_name = 'Feedback/feedback-list.html'
    model = Feedback
    context_object_name = 'all_feedbacks'
