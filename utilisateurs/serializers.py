from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        if user.ecoles and user.ecoles.schema_name:
            token['schema_name'] = user.ecoles.schema_name
            token['id_ecole'] = user.ecoles.id
        else:
            token['schema_name'] = None


        return token
    
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telephone', 'adresse', 'ville_residence', 'ecoles', 'password')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telephone', 'adresse', 'ville_residence')