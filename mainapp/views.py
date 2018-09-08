import datetime

from django.shortcuts import render
from django.urls import reverse
from mimesis import Generic
import random
from .models import Person, Documents
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import Quantity, PersonCreateForm


def index(request):
    context = {
        'quantity': Quantity,
    }
    return render(request, 'mainapp/index.html', context)


def generate(request):
    gender = ('Male', 'Female')
    genreric_info = Generic('ru')
    if request.method == 'POST':
        Person.objects.all().delete()
        quntity = Quantity(request.POST)
        if quntity.is_valid():
            input_data = quntity.cleaned_data['number']
            for t in range(int(input_data)):
                g = random.choices(gender)
                start_of_stud = genreric_info.datetime.datetime(start=2000, end=2010)
                rec = Person(
                    name=genreric_info.person.full_name(),
                    dob=genreric_info.datetime.datetime(start=1980, end=2000),
                    sex=g,
                    cellphone_number=genreric_info.person.telephone(),
                    start_of_studying=start_of_stud,
                    end_of_studying=start_of_stud + datetime.timedelta(days=(365 * 4)),
                    group=random.randrange(1000, 9999),
                    university_name=genreric_info.person.university()
                )
                rec.save()
        return HttpResponseRedirect(reverse('mainapp:index'))


def serch(request):
    pass


def edit(request):
    return render(request, 'mainapp/edit.html')


def create(request):
    if request.method == 'POST':
        created_form = PersonCreateForm(request.POST)
        if created_form.is_valid():
            rec = Person(
                name=created_form.cleaned_data['name'],
                dob=created_form.cleaned_data['dob'],
                sex=created_form.cleaned_data['sex'],
                cellphone_number=created_form.cleaned_data['cellphone_number'],
                start_of_studying=created_form.cleaned_data['start_of_studying'],
                end_of_studying=created_form.cleaned_data['end_of_studying'],
                group=created_form.cleaned_data['group'],
                university_name=created_form.cleaned_data['university_name']
            )
            rec.save()

    create_form = PersonCreateForm()

    context = {
        'create_form': create_form
    }
    return render(request, 'mainapp/create.html', context)
