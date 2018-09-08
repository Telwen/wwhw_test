import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse
from mimesis import Generic
import random
from .models import Person, Documents
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import Quantity, PersonCreateForm, SerchBar


def index(request, page=1):
    persons = Person.objects.all()
    paginator = Paginator(persons, per_page=6)
    try:
        person_paginator = paginator.page(page)
    except PageNotAnInteger:
        person_paginator = paginator.page(1)
    except EmptyPage:
        person_paginator = paginator.page(paginator.num_pages)
    context = {
        'quantity': Quantity,
        'serch_bar': SerchBar,
        'persons': person_paginator
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
                    sex=g[0],
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


def person(request, id):
    person = get_object_or_404(Person, id=id)

    context = {
        'person': person
    }
    return render(request, 'mainapp/person.html', context)


def edit(request, id):
    person= get_object_or_404(Person, id=id)
    if request.method == 'POST':
        edit_form = PersonCreateForm(request.POST, instance=person)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        edit_form = PersonCreateForm(instance=person)
    context = {
        'person': person,
        'edit_form': edit_form
    }
    return render(request, 'mainapp/edit.html', context)


def create(request):
    if request.method == 'POST':
        created_form = PersonCreateForm(request.POST)
        if created_form.is_valid():
            rec = Person(
                name=created_form.cleaned_data['full_name'],
                dob=created_form.cleaned_data['date_of_birth'],
                sex=created_form.cleaned_data['sex'],
                cellphone_number=created_form.cleaned_data['cellphone_number'],
                start_of_studying=created_form.cleaned_data['start_of_studying'],
                end_of_studying=created_form.cleaned_data['end_of_studying'],
                group=created_form.cleaned_data['studing_group'],
                university_name=created_form.cleaned_data['university_name']
            )
            rec.save()

    create_form = PersonCreateForm()

    context = {
        'create_form': create_form
    }
    return render(request, 'mainapp/create.html', context)
