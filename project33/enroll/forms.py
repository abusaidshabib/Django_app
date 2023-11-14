# this is the build in validation for input field 
from django.core import validators
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter your name'})
    email = forms.EmailField(error_messages={'required':'Enter your email'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your password'})
