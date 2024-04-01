from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

# Create your models here.


class Ecoles(TenantMixin):

    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone_1 = models.CharField(max_length=30)
    telephone_2 = models.CharField(max_length=30, blank=True)
    logo = models.ImageField(upload_to="", blank=True)
    adresse = models.CharField(max_length=255)
    ville_residence = models.CharField(max_length=255)
    document = models.FileField(upload_to="", blank=True)
    date_creation = models.DateField()
    date_inscription = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    auto_create_schema = True

    class Meta:
        verbose_name = ('Ecole')
        verbose_name_plural = ('Ecoles')
 
    def __str__(self):
        return self.nom
    
class Domain(DomainMixin):
    pass

