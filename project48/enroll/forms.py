from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# this will help to inheritance the existing signup fields
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # change the label field
        labels = {'email':'Enter your email'}

class EditProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Enter your email'}


class EditAdminProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Enter your email'}