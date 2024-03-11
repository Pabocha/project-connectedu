from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['schema_name'] = user.ecoles.schema_name if user.ecoles else None
        # ...

        return token

# class ResponsableSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password')