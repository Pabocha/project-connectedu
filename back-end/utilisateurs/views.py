from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

# class CustomTokenObtain(TokenObtainPairView):

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)

#         if response.status_code == status.HTTP_200_OK:
#             user = request.user 
#             user_data = {
#             'id': user.id,
#             'username': user.username,
#             # 'email': user.email,
#             # 'ecole': user.ecoles.schema_name if user.ecoles else None,
#             }
#             response.data['user'] = user_data
#         return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'ecole': user.ecoles.schema_name if user.ecoles else None,
    }
    return Response(user_data)
