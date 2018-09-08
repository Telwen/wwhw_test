from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class Quantity(forms.Form):
    number = forms.CharField()


class SerchBar(forms.Form):
    pass


class PersonCreateForm(forms.Form):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = forms.CharField()
    dob = forms.DateField()
    sex = forms.ChoiceField(choices=SEX)
    cellphone_number = forms.CharField()
    start_of_studying = forms.DateField()
    end_of_studying = forms.DateField()
    group = forms.CharField()
    university_name = forms.CharField()