from django.urls import path
from . import views

urlpatterns = [
    path('eleve-create/', views.EleveUploadExcelView.as_view(), name="eleve-create"),
]