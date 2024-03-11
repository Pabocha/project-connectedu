# Generated by Django 5.0 on 2024-02-19 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_ecole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('type_annonce', models.CharField(choices=[('Paiement', 'Paiement'), ('Examen', 'Examen'), ('Autre', 'Autre')], default='Paiement', max_length=255)),
                ('message', models.TextField()),
                ('date_annonce', models.DateTimeField(auto_now_add=True)),
                ('autre_annonce', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Annonce',
                'verbose_name_plural': 'Annonces',
            },
        ),
        migrations.CreateModel(
            name='Appreciations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progression', models.CharField(max_length=255)),
                ('comportement', models.CharField(max_length=255)),
                ('assiduite', models.CharField(max_length=255)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.eleves')),
            ],
            options={
                'verbose_name': 'Appreciation',
                'verbose_name_plural': 'Appreciations',
            },
        ),
        migrations.CreateModel(
            name='Comptables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.eleves')),
            ],
            options={
                'verbose_name': 'Comptable',
                'verbose_name_plural': 'Comptables',
            },
        ),
        migrations.CreateModel(
            name='EmploiDuTemps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'), ('Dimanche', 'Dimanche')], default='Lundi', max_length=255)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.niveaux')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.matieres')),
                ('professeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_ecole.professeurs')),
                ('salle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_ecole.salles')),
            ],
            options={
                'verbose_name': 'Emploi du temps',
                'verbose_name_plural': 'Emploi du temps',
            },
        ),
        migrations.CreateModel(
            name='RelevePresences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_presence', models.DateField()),
                ('liste_presence', models.FileField(upload_to='')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.niveaux')),
            ],
        ),
    ]
