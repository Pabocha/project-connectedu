from django.urls import path, include
from .views import *

urlpatterns = [
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('get-user/', GetUserView.as_view(), name='get-user'),
    path('permission-user/', PermissionView.as_view(), name='permission-user'),
    path('assign-permissions/', AssignPermissionsView.as_view(), name='assign-permissions'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]