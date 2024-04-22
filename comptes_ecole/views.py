import uuid
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import EcoleSerializer
from .models import Ecoles
from django.contrib.auth import get_user_model
from .tasks import send_mail_welcome
from .tasks import execute_migrations
User = get_user_model()


class InscriptionEcole(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # queryset = Ecoles.objects.all()

        password = User.objects.make_random_password()
        print(password)
        # serializer = self.get_serializer(data=request.data)
        serializer = EcoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # extratction des données du responsable 
        nom = serializer.validated_data.pop('nom_responsable')
        prenom = serializer.validated_data.pop('prenom_responsable')
        email = serializer.validated_data.pop('email_responsable')
        instance_ecole = serializer.save()
        
        uuid_responsable = uuid.uuid4()
        uuid_str = str(uuid_responsable)[:5]
        username_responsable = (f"{nom[:3]}-{uuid_str}")
        responsable = User(username=username_responsable, first_name=nom, last_name=prenom, email=email, 
                                        ecoles=instance_ecole)
        responsable.set_password(password)
        responsable.save()

        send_mail_welcome.delay(email, responsable.username, password)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    