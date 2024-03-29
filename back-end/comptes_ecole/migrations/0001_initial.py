# Generated by Django 5.0 on 2024-01-20 02:51

import django.db.models.deletion
import django_tenants.postgresql_backend.base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone_1', models.CharField(max_length=30)),
                ('telephone_2', models.CharField(blank=True, max_length=30)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('adresse', models.CharField(max_length=255)),
                ('ville_residence', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, upload_to='')),
                ('date_creation', models.DateField()),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Ecole',
                'verbose_name_plural': 'Ecoles',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='comptes_ecole.ecoles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
