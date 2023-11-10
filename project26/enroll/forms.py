from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(widget=forms.Textarea)
    # name = forms.CharField(widget=forms.FileInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'addCSS', 'id':'addId'}))
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.HiddenInput)
    first_name = forms.CharField()