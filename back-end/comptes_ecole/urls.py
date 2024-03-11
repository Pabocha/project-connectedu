from django.urls import path
from . import views

urlpatterns = [
    path('ecole/', views.InscriptionEcole.as_view(), name='inscription_ecole'),
    # path('responsable/', views.InscriptionResponsable.as_view(), name='inscription_responsable')
]
