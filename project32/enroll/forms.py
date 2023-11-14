# this is the build in validation for input field 
from django.core import validators
from django import forms

# add some custom validation on build in validation
def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name should start with s')

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(label ='Confirm password', widget=forms.PasswordInput)

    # check password and confirm password
    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valcpwd = self.cleaned_data['cpassword']
        if valcpwd != valpwd:
            raise forms.ValidationError('Password does not match')
    