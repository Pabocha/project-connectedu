from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics, permissions, status, viewsets
# Create your views here.

class EmploiDuTempView(viewsets.ModelViewSet):
    queryset = EmploiDuTemps.objects.all()
    serializer_class = EmploiDuTempSerializer

class AppreciationView(viewsets.ModelViewSet):
    queryset = Appreciations.objects.all()
    serializer_class = AppreciationSerializer

class AnnonceView(viewsets.ModelViewSet):
    queryset = Annonces.objects.all()
    serializer_class = AnnonceSerializer

class RelevePresenceView(viewsets.ModelViewSet):
    queryset = RelevePresences.objects.all()
    serializer_class = RelevePresenceSerializer

class ComptableView(viewsets.ModelViewSet):
    queryset = Comptables.objects.all()
    serializer_class = ComptableSerializer