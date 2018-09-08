from django.shortcuts import render
from django.urls import reverse

from .models import Person, Documents
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import Quantity, PersonCreateForm


def index(request):
    context = {
        'quantity': Quantity,
    }
    return render(request, 'mainapp/index.html', context)


def generate(request):
    if request.method == 'POST':
        quntity = Quantity(request.POST)
        if quntity.is_valid():
            input_data = quntity.cleaned_data['number']
            print(input_data)
        return HttpResponseRedirect(reverse('mainapp:index'))


def serch(request):
    pass


def edit(request):
    return render(request, 'mainapp/edit.html')


def create(request):
    if request.method == 'POST':
        created_form = PersonCreateForm(request.POST)
        print('тут')
        if created_form.is_valid():
            print(created_form.cleaned_data)
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
