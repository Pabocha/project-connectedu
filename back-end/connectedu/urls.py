from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecole/', include('connectedu.routers')),
    path('ecole/v1/',include('gestion_ecole.urls')),
    path('ecole/v2/', include('gestion_ecole.routers')),
    

]
