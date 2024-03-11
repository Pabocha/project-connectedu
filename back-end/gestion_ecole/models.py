from django.db import models

# Create your models here.


    
class Niveaux(models.Model):
    libelle = models.CharField(max_length=255)
    numero = models.IntegerField(blank=True)

    class Meta:
        verbose_name = ("Niveau")
        verbose_name_plural = ("Niveaux")

    def __str__(self):
        return self.libelle
    

class Parents(models.Model):
    nom =models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(unique=True) 
    adresse = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("Parent")
        verbose_name_plural = ("Parents")
    
    def __str__(self):
        return self.nom
    

class Eleves(models.Model):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField() 
    lieu_naissance = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=30)
    niveau = models.ForeignKey(Niveaux,  on_delete=models.SET_NULL, null=True)
    tuteur = models.ForeignKey(Parents, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = ("Eleve")
        verbose_name_plural = ("Eleves")
    
    def __str__(self):
        return self.nom


class Professeurs(models.Model):
    matricule = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=30)
    niveau = models.ManyToManyField(Niveaux)

    class Meta:
        verbose_name = ("Professeur")
        verbose_name_plural = ("Professeurs")

    def __str__(self):
        return self.nom


class Matieres(models.Model):
    libelle = models.CharField(max_length=255)
    coeficient = models.IntegerField()
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeurs, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Matiere")
        verbose_name_plural = ("Matieres")

    def __str__(self):
        return self.libelle


class Salles(models.Model):
    libelle = models.CharField(max_length=20)
    numero = models.IntegerField(blank=True)

    class Meta:
        verbose_name = ("Salle")
        verbose_name_plural = ("Salles")

    def __str__(self):
        return self.libelle




class Notes(models.Model):
    choix_note = [('Devoir', 'Devoir'),
                  ('Examen', 'Examen')]

    matieres = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    type_note = models.CharField(max_length=100, choices=choix_note, default='Devoir')
    note = models.DecimalField(max_digits=10, decimal_places=2)
    eleve = models.ForeignKey(Eleves, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.type_note
    
    # PP4dA8vamj