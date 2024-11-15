from model_utils.models import TimeStampedModel

from django.db import models


class TypeAccount(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name


class Account(TimeStampedModel):
    email = models.EmailField('Email', max_length=50)
    password = models.CharField('Password', max_length=50)
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    phone = models.BigIntegerField('Teléfono', blank=True, null=True)
    address = models.TextField(
        'Dirección',  blank=True, null=True, max_length=50)
    state = models.BooleanField("Activo", default=False)
    company = models.CharField('Empresa', max_length=50)
    age = models.IntegerField('Edad', blank=True, null=True)
    occupation = models.CharField('Empresa', max_length=50)

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
