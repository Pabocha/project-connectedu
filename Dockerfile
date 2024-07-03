# Utilisez l'image Python 3 officielle comme image de base
FROM python:3.11-slim

# Définit les variables d'environnement pour éviter la mise en cache de Python bytecode
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Installez les dépendances du système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Créez le répertoire /app dans le conteneur et définissez le répertoire de travail
RUN mkdir /app
WORKDIR /app

# Copiez le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Mettez à jour pip et installez les dépendances Python à partir du fichier requirements.txt
RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    /env/bin/pip install -r requirements.txt

# Copiez le reste du contenu du répertoire actuel dans /app dans le conteneur
COPY . /app/

# Définissez le chemin d'accès de l'environnement virtuel
ENV PATH="/env/bin:$PATH"

# Exposez le port 8000 pour le serveur Django
EXPOSE 8000

# Commande par défaut pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]







# Utilisez l'image Python 3 officielle comme image de base
# FROM python:3

# # Définit les variables d'environnement pour éviter la mise en cache de Python bytecode
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# # Créez le répertoire /app dans le conteneur
# RUN mkdir /app

# # Définit le répertoire de travail dans le conteneur
# WORKDIR /app

# # Copiez le contenu du répertoire actuel dans /app dans le conteneur
# COPY . /app/

# # Installez les dépendances du système et créez un environnement virtuel
# RUN python -m venv /env

# # Définissez le chemin d'accès de l'environnement virtuel
# ENV PATH="/env/bin:$PATH"

# # Mettez à jour pip et installez les dépendances Python à partir du fichier requirements.txt
# RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiez le script d'entrée dans le conteneur
# COPY entrypoint.sh /app/entrypoint.sh

# Définissez les permissions d'exécution pour le script d'entrée
# RUN chmod +x /app/entrypoint.sh
