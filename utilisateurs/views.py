from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UpdateUserSerializer

User = get_user_model()


class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_info(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'ecole': user.ecoles.schema_name if user.ecoles else None,
    }
    return Response(user_data)
