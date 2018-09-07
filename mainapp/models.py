from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=64)
    dob =
    sex =
    cellphone_number = models.CharField(verbose_name='Cellphone number', max_length=64)
    start_of_studing =
    end_of_studing =
    
    university_name = models.CharField(verbose_name='Name of university', max_length=64)
