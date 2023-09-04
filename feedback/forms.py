from django import forms
from django.forms import TextInput, EmailInput, Textarea

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

        fields = ['first_name', 'last_name', 'email', 'message']

        widgets = {

            'first_name' : TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your first name: '}),
            'last_name' : TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your last name: '}),
            'email' : EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter your email: '}),
            'message' : Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your feedback: '}),



        }


