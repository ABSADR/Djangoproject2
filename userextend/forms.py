from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput

from userextend.models import UserProfile


class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control','placeholder': 'Please enter your password'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture','age','gender','country','zodiac']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'country': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Where you from?'}),
            'zodiac': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'})
        }



class UserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {

            'first_name' : TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
            'last_name' : TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
            'email' : EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email adress'}),
            'username' : TextInput(attrs={'class':'form-control', 'placeholder':'Please enter a username'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter a username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please confirm your password'})