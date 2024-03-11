from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from utilisateurs.views import CustomTokenObtain

# from utilisateurs.views import CustomTokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/info/', include('utilisateurs.urls')),
    path('admin-tenant/', admin.site.urls),
    path('inscription/', include('comptes_ecole.urls')),
    path('contact/', include('contacts.urls')),
]
