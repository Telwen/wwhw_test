from django.conf.urls import url
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('page/<int:page>/', mainapp.index, name='person_page'),
    path('generate/', mainapp.generate, name='generate'),
    path('pesron/<int:id>/', mainapp.person, name='person'),
    path('serch/', mainapp.serch, name='serch'),
    path('create/', mainapp.create, name='create'),
    path('edit/<int:id>/', mainapp.edit, name='edit'),
    path('doc_edit/<int:id>/', mainapp.doc_edit, name='doc_edit'),
    path('doc_add/<int:id>/', mainapp.doc_add, name='doc_add')
]
