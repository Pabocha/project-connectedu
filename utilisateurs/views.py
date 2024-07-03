from rest_framework.response import Response
from rest_framework import status, generics, permissions, views
from django.contrib.auth import get_user_model
from .serializers import UpdateUserSerializer, CreateUserSerializer
from django.contrib.auth.models import Permission, Group
from connectedu.utils import *

User = get_user_model()

class AssignPermissionsView(views.APIView):
    # permission_classes = [IsAdminUser]
    @check_tenant_membership
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        group_name = request.data.get('group_name', 'ACCESS USER')
        permission_ids = request.data.get('permission_ids', [])

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "L'utilisateur spécifié n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({"message": "Le groupe spécifié n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

        if isinstance(permission_ids, int):
            permission_ids = [permission_ids]

        if not permission_ids:  # Ajouter l'utilisateur au groupe avec toutes les permissions
            user.groups.add(group)
        else:  # Ajouter des permissions spécifiques à l'utilisateur sans le mettre dans le groupe
            permissions = Permission.objects.filter(id__in=permission_ids)
            for permission in permissions:
                user.user_permissions.add(permission)

        return Response({"message": "Permissions assignées avec succès"}, status=status.HTTP_200_OK)


class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

class GetUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_responsable = self.request.user
        queryset = User.objects.filter(ecoles=user_responsable.ecoles)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        users_data = list(queryset.values('id', 'username', 'email', 'first_name', 'last_name', 'ecoles'))  # Ajoutez d'autres champs au besoin
        return Response(users_data, status=status.HTTP_200_OK)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin School').exists():
            return Response({"message": "Vous n'avez pas les permissions nécessaires pour créer un utilisateur"}, status=status.HTTP_403_FORBIDDEN)

        # Récupérer l'école de l'utilisateur créateur
        responsable_ecole = request.user.ecoles  

        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = User(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            telephone=data['telephone'],
            adresse=data['adresse'],
            ville_residence=data['ville_residence'],
            ecoles=responsable_ecole  
            )
            user.set_password(data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PermissionView(views.APIView):

    def get(self, request,  format=None):
        try:
            group = Group.objects.get(name="ACCESS USER")
            # group = Group.objects.get(id=group_id)
            permissions = group.permissions.all()
            permissions_data = []
            for permission in permissions:
                permissions_data.append({
                    'id': permission.id,
                    'name': permission.name,
                    'codename': permission.codename,
                })
            return Response(permissions_data, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({"message": "Le groupe spécifié n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

