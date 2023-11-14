from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # this array order is also order the form field
        fields = ['name', 'email', 'password']
        labels={'name':'Enter Name', 'password':'Enter Password', 'email':'Enter Email'}
        help_text = {'name':'Enter Your Full Name'}
        error_message = {'name':{'required':'Naam Likhna Jaruri Hai'}, 'password':{'required':'Password Likhna Jaruri hai'}}
        widgets = {'password':forms.PasswordInput, 'name':forms.TextInput(attrs={'class':'myclass1','placeholder':'Yaha Naam likhe'} )}