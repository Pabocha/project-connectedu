from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import transaction
from .models import Eleves, Parents

@receiver(pre_delete, sender=Eleves)
def delete_eleve(sender, instance, **kwargs):
    try:
        with transaction.atomic():
            tuteur = instance.tuteur

            autres_eleves = Eleves.objects.filter(tuteur=tuteur).exclude(pk=instance.pk)

            if autres_eleves.exists():
                pass
            else:
                tuteur.delete()
    except Exception as e:
        print(f'Erreur inattendue lors de la suppression : {str(e)}')
