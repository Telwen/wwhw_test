import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse
from mimesis import Generic
import random
from .models import Person, Documents
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import Quantity, PersonCreateForm, SerchBar, DocumentCreateForm, DocumentEditForm


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
    doc_type = ['Passport', 'Student_card', 'Drive_license', 'Birth_certificate']
    generated_info = Generic('ru')
    if request.method == 'POST':
        Person.objects.all().delete()
        Documents.objects.all().delete()
        quantity = Quantity(request.POST)
        if quantity.is_valid():
            input_data = quantity.cleaned_data['number']
            for t in range(int(input_data)):
                local_var = 0
                g = random.choice(gender)
                start_of_stud = generated_info.datetime.datetime(start=2000, end=2010)
                per = Person(
                    name=generated_info.person.full_name(),
                    dob=generated_info.datetime.datetime(start=1980, end=2000),
                    sex=g,
                    cellphone_number=generated_info.person.telephone(),
                    start_of_studying=start_of_stud,
                    end_of_studying=start_of_stud + datetime.timedelta(days=(365 * 4)),
                    group=random.randrange(1000, 9999),
                    university_name=generated_info.person.university()
                )
                per.save()
                for d in range(random.randrange(0, 4)):
                    doc = Documents(
                        owner=Person.objects.get(id=per.id),
                        serial_number=random.randrange(10000000, 99999999),
                        date_of_issue=generated_info.datetime.datetime(start=1990, end=2005),
                        type=doc_type[local_var],
                    )
                    local_var += 1
                    doc.save()

        return HttpResponseRedirect(reverse('mainapp:index'))


def serch(request):
    pass


def person(request, id):
    person = get_object_or_404(Person, id=id)
    documents_of_person = Documents.objects.filter(owner=id)
    context = {
        'person': person,
        'documents': documents_of_person
    }
    return render(request, 'mainapp/person.html', context)


def edit(request, id):
    person = get_object_or_404(Person, id=id)
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
            created_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))

    per_create_form = PersonCreateForm()

    context = {
        'per_create_form': per_create_form,
    }
    return render(request, 'mainapp/create.html', context)


def doc_edit(request, id):
    print(id)
    document = get_object_or_404(Documents, id=id)
    if request.method == 'POST':
        edit_form = DocumentEditForm(request.POST, instance=document)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        edit_form = DocumentEditForm(instance=document)
    context = {
        'document': document,
        'edit_form': edit_form
    }
    return render(request, 'mainapp/doc_edit.html', context)


def doc_add(request, id):
    if request.method == 'POST':
        created_form = DocumentCreateForm(request.POST)
        if created_form.is_valid():
            form_data = created_form.cleaned_data
            doc = Documents(
                owner=Person.objects.get(id=id),
                serial_number=form_data['serial_number'],
                date_of_issue=form_data['date_of_issue'],
                type=form_data['type'],
                scan_of_document=form_data['scan_of_document']
            )
            doc.save()
            return HttpResponseRedirect(reverse('mainapp:index'))

    create_form = DocumentCreateForm()

    context = {
        'person_id': id,
        'create_form': create_form,
    }

    return render(request, 'mainapp/doc_add.html', context)
