from django.db import models
from django.contrib.auth.models import AbstractUser
from comptes_ecole.models import Ecoles
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.

class Utilisateurs(AbstractUser):
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=255)
    ville_residence = models.CharField(max_length=255)
    ecoles = models.ForeignKey(Ecoles, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ('Utilisateur')
        verbose_name_plural = ('Utilisateurs')


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    # email_plaintext_message = "{}?token={}".format(
    #         instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
    #         reset_password_token.key)
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:3000/reset-password/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Crediation portal account"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )