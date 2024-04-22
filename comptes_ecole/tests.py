from django.test import TestCase
from django_tenants.utils import get_public_schema_name
from .models import Ecoles, Domain
from django.conf import settings
from django.core.management import call_command


class CreatePublicTenantTestCase(TestCase):
    def test_create_public_tenant(self):
        # Assurez-vous que le tenant public n'existe pas avant l'exécution de la fonction
        self.assertFalse(Ecoles.objects.filter(schema_name=get_public_schema_name()).exists())

        # # Appelez la fonction pour créer le tenant public
        call_command('makemigrations')
        call_command('migrate')
        # create_public_tenant(sender=None)

        # Vérifiez que le tenant public a été créé avec les attributs attendus
        public_tenant = Ecoles.objects.get(schema_name=get_public_schema_name())
        self.assertEqual(public_tenant.nom, 'ConnectEdu')
        self.assertTrue(public_tenant.active)

        # Vérifiez également que le domaine a été associé correctement au tenant public
        public_domain = Domain.objects.get(domain=settings.BASE_DOMAIN)
        self.assertEqual(public_domain.tenant, public_tenant)
