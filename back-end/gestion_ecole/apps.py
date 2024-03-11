from django.apps import AppConfig


class GestionEcoleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion_ecole'

    def ready(self):
        import gestion_ecole.signals