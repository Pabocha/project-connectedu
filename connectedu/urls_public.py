from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('utilisateur/', include('utilisateurs.urls')),
    path('admin-tenant/', admin.site.urls),
    path('ecole/', include('comptes_ecole.urls')),
    path('contact/', include('contacts.urls')),
    path('documentation/', include('documentation.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
