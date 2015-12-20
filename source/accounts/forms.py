from django import forms
from django.contrib.auth import authenticate

from .models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField(error_messages={'required': 'Please enter your first name.'})
    last_name = forms.CharField(error_messages={'required': 'Please enter your last name.'})
    email = forms.EmailField(error_messages={'required': 'Please enter your email.',
                                             'invalid': 'Please enter a valid email.'}) 
    password = forms.CharField(widget=forms.PasswordInput,
                                error_messages={'required': 'Please enter your password.'})
    reenter_password = forms.CharField(widget=forms.PasswordInput, 
                                        error_messages={'required': 'Please reenter your password.'})

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        rennter_password = cleaned_data.get('reenter_password')

        if password and rennter_password:
            if password != rennter_password:
                self.add_error('password', "Your passwords did not match. Try again.")
        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            self.add_error('password', 'Your password must be at least 6 characters.')

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'That email is already being used. Try again.')
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required': 'Please enter your email.'})
    password = forms.CharField(widget=forms.PasswordInput,
                                error_messages={'required': 'Please enter your password.'})

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            self.add_error('email', 'Invalid email or password.')
        return cleaned_data
