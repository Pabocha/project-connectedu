
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Ecoles, Domain
from django.conf import settings
from django.contrib.sites.models import Site
from unidecode import unidecode


# Creation automatique du schema de l'école et de son domain 
def create_schema_and_domain_school(instance, created):
    instance.schema_name = f"{unidecode(instance.nom.lower().replace(' ', '_'))}"
    if created:
        domain = unidecode(instance.nom.lower().replace(' ', '-'))
        domain = f"{domain}.{settings.BASE_DOMAIN}"
        primary_key = True
        tenant_id = instance.id
        Domain.objects.create(domain=domain, is_primary=primary_key, tenant_id=tenant_id)
        Site.objects.create(domain=domain, name=domain)



# pour la creation du schema avant sauvegarde dans la base de données
@receiver(pre_save, sender=Ecoles)
def pre_save_school(sender, instance, **kwargs):
    create_schema_and_domain_school(instance, False)

# pour la creation après sauvegarde dans la base de ddonnées 
@receiver(post_save, sender=Ecoles)
def post_save_school(sender, instance, created, **kwargs):
    create_schema_and_domain_school(instance, created)