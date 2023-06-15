from tkinter import Widget

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class CustomerCreationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "passwords1": forms.PasswordInput(attrs={"class": "form-control"}),
            "passwords2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
