# from celery import shared_task
from connectedu.celery import app
from django.core.management import call_command
from django.core.mail import send_mail
from django.conf import settings
from .models import Ecoles
from django_tenants.utils import schema_context


@app.task
def send_mail_welcome(email, responsable, password):
    # Titre du message
    subject = "Message de bienvenue de l'équipe ConnectEdu"
    # Corps du message
    message = ("Bienvenue sur notre plateforme et merci de s'être inscris ci-desous vous trouverez vos informations de connexion \n\n" +
            "Nom d'utilisateur : " + responsable + "\n Mot de passe : " + password)

    # Nom et adresse e-mail de l'expéditeur
    sender = "ConnectEdu <{}>".format(settings.EMAIL_HOST_USER)

    # Adresse e-mail du destinataire
    recipient = [email]
    send_mail(
        subject,
        message,
        sender,
        recipient,
        fail_silently=False
    )

@app.task
def execute_migrations(schema_name):
    # Exécuter les migrations sur le schéma spécifié
    with schema_context(schema_name):
        # Exécuter les migrations
        call_command('migrate', verbosity=0)