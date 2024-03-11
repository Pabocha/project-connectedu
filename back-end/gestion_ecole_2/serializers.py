from rest_framework import serializers
from .models import *

class EmploiDuTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmploiDuTemps
        fields = ('__all__')

class AppreciationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appreciations
        fields = ('__all__')

class AnnonceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annonces
        fields = ('__all__')