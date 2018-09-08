from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class Quantity(forms.Form):
    number = forms.CharField()


class SerchBar(forms.Form):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    sex = forms.ChoiceField(choices=SEX)
    cellphone_number = forms.CharField()
    start_of_studying = forms.DateField()
    end_of_studying = forms.DateField()
    studing_group = forms.CharField()
    university_name = forms.CharField()
    passport_number = forms.CharField()


class PersonCreateForm(forms.Form):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    sex = forms.ChoiceField(choices=SEX)
    cellphone_number = forms.CharField()
    start_of_studying = forms.DateField()
    end_of_studying = forms.DateField()
    studing_group = forms.CharField()
    university_name = forms.CharField()