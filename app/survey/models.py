from model_utils.models import TimeStampedModel
from django.db import models
from ..account.models import *


class Survey(TimeStampedModel):

    name = models.TextField("Nombre", blank=True, null=True)
    state = models.BooleanField("Activo", default=False)
    

    def __str__(self):
        return f'{self.name} - {self.state}'


class Questions(TimeStampedModel):

    name = models.TextField("Pregunta", blank=True, null=True)
    op1 = models.CharField("Opcion 1", max_length=10, blank=True, null=True)
    op2 = models.CharField("Opcion 1", max_length=10, blank=True, null=True)

    Survey = models.ForeignKey(
        Survey,
        verbose_name="Survey",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
   
    def __str__(self):
        return self.name


class Responses(TimeStampedModel):

    response = models.TextField("Respuesta", blank=True, null=True)
    question = models.ForeignKey(
        Questions,
        verbose_name="Questions",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    account = models.ForeignKey(
        Account,
        verbose_name="Account",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
   
    def __str__(self):
        return self.response