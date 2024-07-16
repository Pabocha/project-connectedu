
from django.db.models.signals import pre_save, post_save, post_migrate
from django.dispatch import receiver
from .models import Ecoles, Domain
from django.conf import settings
from django.contrib.sites.models import Site
from unidecode import unidecode


@receiver(post_migrate)
def create_school_after_migration(sender, **kwargs):

    if sender.name == 'comptes_ecole':
        if not Ecoles.objects.filter(schema_name__iexact="public").exists():
            ecole = Ecoles.objects.create(
                schema_name = 'public',
                nom = 'ConnectEdu',
                email = 'connectedu@gmail.com',
                telephone_1 = '069493272',
                adresse = 'Pointe Noire',
                ville_residence = 'Siafoumou', 
                date_creation = '2020-04-05',
            )
            ecole.save()
            domain = Domain.objects.create(domain=settings.BASE_DOMAIN, tenant_id=ecole.id)
            domain.save()
            Site.objects.create(domain=domain, name=ecole.nom)




# Creation automatique du schema de l'école et de son domain 
def create_schema_and_domain_school(instance, created, **kwargs):
    if instance.schema_name != 'public':
        instance.schema_name = f"{unidecode(instance.nom.lower().replace(' ', '_'))}"
        if created:
            domain = unidecode(instance.nom.lower().replace(' ', '-'))
            domain = f"{domain}.{settings.BASE_DOMAIN}"
            primary_key = True
            tenant_id = instance.id
            Domain.objects.create(domain=domain, is_primary=primary_key, tenant_id=tenant_id)
            Site.objects.create(domain=domain, name=domain)
    else:
        Site.objects.create(domain=settings.BASE_DOMAIN, name=instance.nom)



# pour la creation du schema avant sauvegarde dans la base de données
@receiver(pre_save, sender=Ecoles)
def pre_save_school(sender, instance, **kwargs):
    create_schema_and_domain_school(instance, False)

# pour la creation après sauvegarde dans la base de ddonnées 
@receiver(post_save, sender=Ecoles)
def post_save_school(sender, instance, created, **kwargs):
    create_schema_and_domain_school(instance, created, **kwargs)


