# Generated by Django 5.0 on 2024-03-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_ecole', '0004_alter_eleves_matricule_alter_professeurs_matricule'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
