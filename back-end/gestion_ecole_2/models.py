from django.db import models
from gestion_ecole.models import *

# Create your models here.

class Appreciations(models.Model):
    eleve = models.ForeignKey(Eleves, on_delete=models.CASCADE)
    progression = models.CharField(max_length=255)
    comportement = models.CharField(max_length=255)
    assiduite = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Appreciation')
        verbose_name_plural = ('Appreciations')

    def __str__(self):
        return self.progression
    

class Comptables(models.Model):

    eleve = models.ForeignKey(Eleves, on_delete=models.CASCADE)
    mois = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ("Comptable")
        verbose_name_plural = ("Comptables")

    def __str__(self):
        return self.mois
    

class RelevePresences(models.Model):
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    date_presence = models.DateField()
    liste_presence = models.FileField(upload_to="")


class Annonces(models.Model):
    choix_annonce = [
        ('Paiement', 'Paiement'),
        ('Examen', 'Examen'),
        ('Autre', 'Autre'),
    ]

    titre = models.CharField(max_length=255)
    type_annonce = models.CharField(max_length=255, choices=choix_annonce, default='Paiement')
    message = models.TextField()
    date_annonce = models.DateTimeField(auto_now_add=True)
    autre_annonce = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = ("Annonce")
        verbose_name_plural = ("Annonces")

    def __str__(self):
        return self.titre
    
class EmploiDuTemps(models.Model):
    choix_jour = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    jour = models.CharField(max_length=255, choices=choix_jour, default='Lundi')
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    classe = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeurs, on_delete=models.SET_NULL, null=True)
    salle = models.ForeignKey(Salles, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Emploi du temps")
        verbose_name_plural = ("Emploi du temps")

    def __str__(self):
        return self.jour