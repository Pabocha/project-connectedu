# FROM python:3

# ENV PYTHONBUFFERD 1

# ENV PYTHONDONTWRTEBYTECODE 1

# RUN mkdir /app 

# WORKDIR /app

# COPY . /app/

# RUN python -m venv /env

# ENV PATH = "/env/bin/:$PATH"

# RUN python -m pip install --upgrade pip

# COPY requirements.txt /app/

# RUN pip install -r requirements.txt

# Utilisez une image de base avec Python
FROM python:3.

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste de l'application dans le conteneur
COPY . .

# Exposez le port sur lequel Django s'exécutera
EXPOSE 8000

# Commande pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
