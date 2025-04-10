from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class AuthenticationRestController(APIView):
    def get(self, request):
        return Response({"articles": ""})
    
    def post(self, request):
        admin_group, created = Group.objects.get_or_create(name='ddd_admin')
        analyst_group, created = Group.objects.get_or_create(name='ddd_analyst')
        playlist_creator_group, created = Group.objects.get_or_create(name='ddd_playlist_creator')

        content_type = ContentType.objects.get_for_model(User)
        perm_admin, created = Permission.objects.get_or_create(
            codename='can_manage_all', name='Peut avoir un apperçu de toute l\'application', content_type=content_type
        )
        perm_analyst, created = Permission.objects.get_or_create(
            codename='can_analys', name='Peut voir les rapports', content_type=content_type
        )
        perm_playlist_creator, created = Permission.objects.get_or_create(
            codename='can_create_playlists', name='Peut créer des playlists', content_type=content_type
        )

        if not admin_group.permissions.contains(perm_admin):
            admin_group.permissions.add(perm_admin)
        if not analyst_group.permissions.contains(perm_analyst):
            analyst_group.permissions.add(perm_analyst)
        if not playlist_creator_group.permissions.contains(perm_playlist_creator):
            playlist_creator_group.permissions.add(perm_playlist_creator)

        if not User.objects.filter(username='admin').exists():
            admin_user, created = User.objects.get_or_create(username='admin', email='admin@example.com', password='admin')
            admin_user.groups.add(admin_group)
        if(not User.objects.filter(username='analyst').exists()):
            analyst_user, created = User.objects.get_or_create(username='analyst', email='analyst@example.com', password='analyst')
            analyst_user.groups.add(analyst_group)
        if(not User.objects.filter(username='playlist_creator').exists()):
            playlist_creator_user, created = User.objects.get_or_create(username='playlist_creator', email='playlist_creator@example.com', password='playlist_creator')
            playlist_creator_user.groups.add(playlist_creator_group)
        
        return Response({"message": "POST - Création d’un utilisateur"}, status=status.HTTP_201_CREATED)