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
    niveau = serializers.IntegerField(write_only=True)

    class Meta:
        model = Matieres
        fields = ('libelle', 'coeficient', 'niveau')


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveaux
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="parent-detail",
                                               read_only=True, lookup_field="pk")
    class Meta:
        model = Parents
        fields = '__all__'

class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleves
        fields = '__all__'

class EleveCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="eleve-detail",
                                               read_only=True, lookup_field="pk")
    # parent = ParentSerializer()
    parent_nom = serializers.CharField(write_only=True)
    parent_prenom = serializers.CharField(write_only=True)
    parent_telephone = serializers.CharField(write_only=True)
    parent_email = serializers.EmailField(write_only=True)
    parent_adresse = serializers.CharField(write_only=True)

    matricule = serializers.CharField(read_only=True)
    class Meta:
        model = Eleves
        fields = ('url', 'matricule', 'nom', 'prenom', 'date_naissance', 'lieu_naissance', 'adresse', 'telephone', 
                   'parent_nom', 'parent_prenom', 'parent_telephone', 'parent_email', 'parent_adresse')



    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        # Ajoutez d'autres champs à mettre à jour si nécessaire
        instance.save()
        return instance

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'