#!/bin/bash

set -e

# Activez l'environnement virtuel
source /env/bin/activate

# Vérifiez le premier argument passé au script
if [ "$1" == 'gunicorn' ]; then
    # Si le premier argument est 'gunicorn', exécutez Gunicorn
    exec gunicorn connectedu.wsgi:application -b 0.0.0.0:8000
else
    # Sinon, exécutez le serveur de développement Django
    exec python manage.py runserver 0.0.0.0:8000
fi
