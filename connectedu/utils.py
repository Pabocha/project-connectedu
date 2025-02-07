from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django_tenants.utils import get_tenant_model


def check_tenant_membership(view_func):
    @wraps(view_func)
    def _wrapped_view(view, request, *args, **kwargs):
        user = request.user
        tenant_model = get_tenant_model()
        domain_url = request.get_host().split(':')[0]
        if domain_url.startswith('www.'):
            domain_url = domain_url[4:]

        try:
            tenant = tenant_model.objects.get(domains__domain=domain_url)
        except tenant_model.DoesNotExist:
            return Response({"message": "Aucun tenant trouvé pour ce domaine"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.ecoles != tenant:
            return Response({"message": "Vous n'êtes pas autorisé à accéder à cet ecole"}, status=status.HTTP_403_FORBIDDEN)

        return view_func(view, request, *args, **kwargs)
    return _wrapped_view

