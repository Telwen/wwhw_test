from django.conf.urls import url
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('generate/', mainapp.generate, name='generate'),
    path('serch/', mainapp.serch, name='serch'),
    path('create/', mainapp.create, name='create'),
    path('edit/', mainapp.edit, name='edit')
]
