from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group, Permission
from rest_framework.authtoken.models import Token
from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ViewSet

class AuthenticationRestController(ViewSet):
    def delete(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({'detail': 'Token correctement supprimé.'}, status=status.HTTP_200_OK)

    def get_user_groups(self, request):
        user = request.user
        groups = user.groups.values_list('name', flat=True)
        return Response({'groups': list(groups)})