from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField()
    # options
    name = forms.CharField(min_length=5, max_length=50, strip=False, empty_value='Default', error_messages={'required':'Enter your Name'})
    agree = forms.BooleanField(label_suffix=' ', label='I Agree')
    roll = forms.IntegerField()
    float = forms.FloatField()
    decimal = forms.DecimalField(max_value=40, min_value=5, max_digits=4, decimal_places=1)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    comment = forms.SlugField()
    website= forms.URLField(min_length=5, max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
    description=forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class':'css1 css2', 'id':'id1'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))    
