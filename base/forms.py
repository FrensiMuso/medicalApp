from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class PatientCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


