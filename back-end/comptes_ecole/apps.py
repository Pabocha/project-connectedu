from django.apps import AppConfig


class ComptesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comptes_ecole'

    def ready(self):
        import comptes_ecole.signals