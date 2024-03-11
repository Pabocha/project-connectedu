from django.urls import path 
from . import views

urlpatterns = [
    path('news-letters/', views.NewsLetterView.as_view(), name='newsletters'),
    path('send-single-email/', views.SingleEmailView.as_view(), name='send-single-email'),
    path('send-multiple-email/', views.MultipleEmailView.as_view(), name='send-multiple-email')
]