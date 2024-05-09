from .settings import *

DEBUG = False 

ALLOWED_HOSTS = ['*']

BASE_DOMAIN = 'connectedut-807b56b6599b.herokuapp'

DATABASES['default'] = dj_database_url.config(engine='django_tenants.postgresql_backend')

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

django_heroku.settings(locals())
