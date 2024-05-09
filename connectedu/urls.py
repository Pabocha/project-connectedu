from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from comptes_ecole.views import EcoleInfoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecole/', include('connectedu.routers')),
    path('ecole/v1/',include('gestion_ecole.urls')),
    path('ecole/v2/', include('gestion_ecole.routers')),
    path('info-ecole/<int:pk>/', EcoleInfoView.as_view(), name='info-ecole'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)