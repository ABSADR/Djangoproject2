from django.forms import TextInput, EmailInput, Textarea, DateInput
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = ['first_name', 'last_name', 'email', 'request']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'request': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your request',
                                       'rows': 3}),


        }

        # def clean(self):
        #     cleaned_data = self.cleaned_data
        #     get_email = cleaned_data.get('email')
