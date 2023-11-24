from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# this will help to inheritance the existing signup fields
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # change the label field
        labels = {'email':'Enter your email'}