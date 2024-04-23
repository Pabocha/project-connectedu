from django.urls import path, include
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', user_info, name='user_info'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]