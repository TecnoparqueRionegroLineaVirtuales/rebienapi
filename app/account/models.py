from model_utils.models import TimeStampedModel

from django.db import models


class TypeAccount(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name


class Account(TimeStampedModel):
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    password = models.CharField('Password', max_length=50, blank=True, null=True)
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    phone = models.BigIntegerField('Teléfono', blank=True, null=True)
    address = models.TextField(
        'Dirección',  blank=True, null=True, max_length=50)
    state = models.BooleanField("Activo", default=False)
    company = models.CharField('Empresa', max_length=50)
    birthdate = models.DateField('Fecha Nacimiento', blank=True, null=True)
    occupation = models.CharField('Empresa', max_length=50)
    city  = models.CharField('Ciudad', max_length=50, blank=True, null=True)
    gender = models.CharField('Género',  max_length=2, blank=True, null=True)
    type_doc = models.CharField('Tipo de documento',  max_length=2, blank=True, null=True)
    identity = models.BigIntegerField('Identificación', blank=True, null=True)
    work_area = models.CharField('Area de trabajo', max_length=50, blank=True, null=True)
    compensation_box = models.CharField('Caja de compensación', max_length=50, blank=True, null=True)
    stature = models.FloatField('Estatura', blank=True, null=True)
    weight = models.IntegerField('Peso', blank=True, null=True)
    imc = models.FloatField('IMC', max_length=50, blank=True, null=True)
    

    type_account = models.ForeignKey(
        TypeAccount,
        verbose_name="Type account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=1,
    )

    def __str__(self):

        return f'{self.email} - {self.name} {self.last_name} - {self.type_account} '
