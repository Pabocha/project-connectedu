from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import EcoleSerializer
from .models import Ecoles
from django.contrib.auth import get_user_model
from .tasks import send_mail_welcome
from .tasks import execute_migrations
User = get_user_model()


class InscriptionEcole(generics.ListCreateAPIView):

    queryset = Ecoles.objects.all()
    serializer_class = EcoleSerializer

    def create(self, request, *args, **kwargs):
        """
        Je crée un mot de passe avec make_random_password puis ce mot de passe est assigné à l'utilisateur 
        crée avet le set_passord
        """
        password = User.objects.make_random_password()
        print(".....voilà un peu")
        print(password)
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        # extratction des données du responsable 
        nom = serializer.validated_data.pop('nom_responsable')
        prenom = serializer.validated_data.pop('prenom_responsable')
        email = serializer.validated_data.pop('email_responsable')
        instance_ecole = serializer.save()
    
        responsable = User(username=f"{nom}-OG", first_name=nom, last_name=prenom, email=email, 
                                        ecoles=instance_ecole)
        responsable.set_password(password)
        responsable.save()

        send_mail_welcome.delay(email, responsable.username, password)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    