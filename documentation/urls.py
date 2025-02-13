from django.urls import path
from . import views



urlpatterns =[
    path('note', views.note_doc, name='note'),
    path('api', views.api_doc, name='api'),
    path('utilisateur', views.utilisateur_doc, name='utilisateur')
]