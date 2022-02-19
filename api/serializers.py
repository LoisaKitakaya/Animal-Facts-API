from rest_framework import serializers
from .models import AnimalFact

class AnimalFactSerializer(serializers.ModelSerializer):

    class Meta:

        model = AnimalFact

        fields = '__all__'