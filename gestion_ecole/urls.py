from django.urls import path
from . import views

urlpatterns = [
    path('create-eleve-excel/', views.EleveUploadExcelView.as_view(), name="create-eleve-excel"),
    path('total-eleve/', views.get_total_eleves, name="total-eleve"),
]