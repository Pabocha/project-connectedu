from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.InscriptionEcole.as_view(), name='inscription_ecole'),
    path('doc/', views.ecole_doc, name='doc_ecole'),
]
