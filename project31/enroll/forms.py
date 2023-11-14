# this is the build in validation for input field 
from django.core import validators
from django import forms

# add some custom validation on build in validation
def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name should start with s')

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(validators=[starts_with_s])
    email = forms.EmailField()
    