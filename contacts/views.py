from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import NewsLetters
from .serializer import NewsLetterSerializer, EmailSerializer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class NewsLetterView(generics.CreateAPIView):

    queryset = NewsLetters.objects.all()
    serializer_class = NewsLetterSerializer

class SingleEmailView(generics.CreateAPIView):

    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sender = "ConnectEdu <{}>".format(settings.EMAIL_HOST_USER)
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        recepteur = serializer.validated_data['recepteur'][0]

        send_mail(
        subject,
        message,
        sender,
        [recepteur],
        fail_silently=False,
        )
 
        return Response({'message': 'Email envoyé avec succès'}, status=status.HTTP_200_OK)
    
class MultipleEmailView(generics.CreateAPIView):
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sender = "ConnectEdu <{}>".format(settings.EMAIL_HOST_USER)
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        recepteur = serializer.validated_data['recepteur']

        send_mail(
        subject,
        message,
        sender,
        recepteur,
        fail_silently=False,
        )

        # send_mail(subject, message, settings.EMAIL_HOST_USER, recepteur)

        return Response({'message': 'Email envoyé avec succès'}, status=status.HTTP_200_OK)