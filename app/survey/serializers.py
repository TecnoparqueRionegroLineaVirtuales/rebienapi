from rest_framework import serializers
from .models import *

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('__all__')

class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('__all__')

class ResponsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responses
        fields = ('__all__')
