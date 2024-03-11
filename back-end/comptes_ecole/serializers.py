from rest_framework import serializers
from .models import Ecoles
from django.contrib.auth import get_user_model

User = get_user_model()

class ResponsableSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class EcoleSerializer(serializers.ModelSerializer):

    nom_responsable = serializers.CharField(write_only=True)
    prenom_responsable = serializers.CharField(write_only=True)
    email_responsable = serializers.EmailField(write_only=True)


    class Meta:
        model = Ecoles
        fields = ('nom', 'email', 'telephone_1', 'telephone_2', 'adresse', 'ville_residence', 'logo', 'date_creation', 'document', 
                  'nom_responsable', 'prenom_responsable', 'email_responsable')
        
   
