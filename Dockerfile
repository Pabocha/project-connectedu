# Utilisez l'image Python 3 officielle comme image de base
FROM python:3

# Définit les variables d'environnement pour éviter la mise en cache de Python bytecode
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Créez le répertoire /app dans le conteneur
RUN mkdir /app

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire actuel dans /app dans le conteneur
COPY . /app/

# Installez les dépendances du système et créez un environnement virtuel
RUN python -m venv /env

# Définissez le chemin d'accès de l'environnement virtuel
ENV PATH="/env/bin:$PATH"

# Mettez à jour pip et installez les dépendances Python à partir du fichier requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiez le script d'entrée dans le conteneur
# COPY entrypoint.sh /app/entrypoint.sh

# Définissez les permissions d'exécution pour le script d'entrée
# RUN chmod +x /app/entrypoint.sh
