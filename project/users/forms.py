from django import forms
from django.contrib.auth.forms import UserCreationForm

from models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a custom user with privileges, from the given email and
    password
    """
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        # We do this because, by default django requires password1 & password2.
        # But in our case, we only want the user to enter password once.
        self.fields.pop('password2')

    class Meta:
        model = CustomUser
        fields = ("name", "email", "password1")


class AuthForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)