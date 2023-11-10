from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='initial_value', help_text="help text as a message error etc")
    email = forms.EmailField()
    first_name = forms.CharField()