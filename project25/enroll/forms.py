from django import forms
class StudentRegistration(forms.Form):
    # label will change your label, label_suffix help to change the : on form
    name = forms.CharField(label='Your Name', label_suffix=' ', required=False, disabled=True, help_text='Limit 70 Char')
    email = forms.EmailField()
    mobile = forms.IntegerField()
    first_name = forms.CharField()
    # this is hidden field
    key = forms.CharField(widget=forms.HiddenInput())