from django.db import models


class Person(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    name = models.CharField(verbose_name='Name, middle name and last name', max_length=64)
    dob = models.DateField(verbose_name='Date of birth')
    sex = models.CharField(verbose_name='Sex of person', max_length=64, choices=SEX)
    cellphone_number = models.CharField(verbose_name='Cellphone number', max_length=64)
    start_of_studying = models.DateField(verbose_name='Start of studying')
    end_of_studying = models.DateField(verbose_name='End of studying')
    group = models.CharField(verbose_name='Studying group', max_length=64)
    university_name = models.CharField(verbose_name='Name of university', max_length=64)

    def str(self):
        return self.name


class Documents(models.Model):
    DOCUMENT_TYPE = (
        ('Birth_certificate', 'Birth certificate'),
        ('Passport', 'Passport'),
        ('Student_card', 'Student card'),
        ('Drive_license', 'Drive license'),

    )
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    serial_number = models.CharField(verbose_name='Serial number of document', max_length=64, unique=True)
    date_of_issue = models.DateField(verbose_name='Date of issue')
    type = models.CharField(verbose_name='Document type', max_length=64, choices=DOCUMENT_TYPE)
    scan_of_document = models.ImageField(upload_to='products_images', blank=True)

    def str(self):
        return "{} ({})".format(self.owner.name, self.type)
