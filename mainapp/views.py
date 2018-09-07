from django.shortcuts import render
from .models import Person, Documents
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import Quantity


def index(request):
    if request.method == 'POST':
        quntity = Quantity(request.POST)
        if quntity.is_valid():
            input_data = quntity.cleaned_data['number']
    context = {
        'quantity': Quantity,
    }
    return render(request, 'mainapp/index.html', context)


def edit(request):
    return render(request, 'mainapp/edit.html')


def create(request):
    return render(request, 'mainapp/create.html')
