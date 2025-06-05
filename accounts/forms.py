from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BlogUserLogInForm(AuthenticationForm):
    pass


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    phone = forms.CharField(required=False, max_length=15, label="N° de tél.")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "phone"
        )
