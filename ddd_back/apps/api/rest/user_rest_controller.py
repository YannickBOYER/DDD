from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

class IsAdminGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.groups.filter(name='admin').exists()
        )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminGroup]
    http_method_names = ['get', 'delete']

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        data = [
            {
                'id': u.id,
                'username': u.username,
                'email': u.email,
                'groups': list(u.groups.values_list('name', flat=True)),
            } for u in users
        ]
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)