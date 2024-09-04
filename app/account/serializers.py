from rest_framework import serializers
from .models import Account, TypeAccount


class TypeAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeAccount
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):

    type_account = TypeAccountSerializer(read_only=True)
    type_account_id = serializers.IntegerField(required=False)

    class Meta:
        model = Account
        fields = ('__all__')
