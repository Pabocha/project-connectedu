from django.db import models
from django.contrib.auth.models import AbstractUser
from comptes_ecole.models import Ecoles

# Create your models here.

class Utilisateurs(AbstractUser):
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=255)
    ville_residence = models.CharField(max_length=255)
    ecoles = models.ForeignKey(Ecoles, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ('Utilisateur')
        verbose_name_plural = ('Utilisateurs')
