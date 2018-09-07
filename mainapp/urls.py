from django.conf.urls import url
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    url(r'^$', mainapp.index, name='index'),
    url(r'^create/$', mainapp.create, name='create'),
    url(r'^edit/$', mainapp.edit, name='edit')
]
