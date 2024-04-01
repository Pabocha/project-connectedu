from rest_framework import serializers
from .models import *


class SalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salles
        fields = ('__all__')

class ProfesseurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professeurs
        fields = ('__all__')

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matieres
        fields = ('__all__')


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveaux
        fields = '__all__'

class EleveSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="eleve-detail",
                                               read_only=True, lookup_field="pk")
    class Meta:
        model = Eleves
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="parent-detail",
                                               read_only=True, lookup_field="pk")
    class Meta:
        model = Parents
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'