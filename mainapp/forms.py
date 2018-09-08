from django import forms
from .models import Person
from django.forms import ModelForm


class Quantity(forms.Form):
    number = forms.CharField()
    number.widget.attrs['class'] = 'form-control'
    number.help_text = ''


class SerchBar(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'sex', 'cellphone_number',
                  'start_of_studying', 'end_of_studying', 'group', 'university_name']


class PersonCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'cellphone_number',
                  'start_of_studying', 'end_of_studying', 'group', 'university_name']

