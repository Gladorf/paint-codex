from rest_framework import serializers
from .models import Figurine, Step

class FigurineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figurine
        fields = ['id', 'nom']


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'figurine', 'description', 'outil', 'ordre']
