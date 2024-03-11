from django.db import models

# Create your models here.


class NewsLetters(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "News Letters"
        verbose_name_plural = "News Letters"

    def __str__(self):
        return self.nom