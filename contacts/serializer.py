from rest_framework import serializers
from .models import NewsLetters


class NewsLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsLetters
        fields = ("__all__")

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recepteur = serializers.ListField(child=serializers.EmailField())

 