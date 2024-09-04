from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, TypeAccount
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class AccountViewset(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class TypeAccountViewset(viewsets.ModelViewSet):

    queryset = TypeAccount.objects.all()
    serializer_class = TypeAccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')

