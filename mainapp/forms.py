from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class Quantity(forms.Form):
    number = forms.CharField()
