# Generated by Django 5.0 on 2024-02-19 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Niveaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('numero', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Niveau',
                'verbose_name_plural': 'Niveaux',
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(max_length=255)),
                ('mot_de_passe', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Salles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('numero', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Salle',
                'verbose_name_plural': 'Salles',
            },
        ),
        migrations.CreateModel(
            name='Matieres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('coeficient', models.IntegerField()),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.niveaux')),
            ],
            options={
                'verbose_name': 'Matiere',
                'verbose_name_plural': 'Matieres',
            },
        ),
        migrations.CreateModel(
            name='Eleves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=30)),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_ecole.niveaux')),
                ('titeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_ecole.parents')),
            ],
            options={
                'verbose_name': 'Eleve',
                'verbose_name_plural': 'Eleves',
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_note', models.CharField(choices=[('Devoir', 'Devoir'), ('Examen', 'Examen')], default='Devoir', max_length=100)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.eleves')),
                ('matieres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_ecole.matieres')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.CreateModel(
            name='Professeurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=30)),
                ('niveau', models.ManyToManyField(to='gestion_ecole.niveaux')),
            ],
            options={
                'verbose_name': 'Professeur',
                'verbose_name_plural': 'Professeurs',
            },
        ),
        migrations.AddField(
            model_name='matieres',
            name='professeur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_ecole.professeurs'),
        ),
    ]
