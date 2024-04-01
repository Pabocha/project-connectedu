from django.urls import path, include
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', user_info, name='user_info'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('reset-password', views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_send', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset_password_complete', views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]