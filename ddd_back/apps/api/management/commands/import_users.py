from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Importe des utilisateurs avec des groupes et des permissions"

    def handle(self, *args, **kwargs):
        # Créer les groupes
        admin_group, created = Group.objects.get_or_create(name='admin')
        analyst_group, created = Group.objects.get_or_create(name='analyst')
        playlist_creator_group, created = Group.objects.get_or_create(name='playlist_creator')

        # Créer les permissions
        content_type = ContentType.objects.get_for_model(User)
        perm_admin, created = Permission.objects.get_or_create(
            codename='can_manage_all', name="Peut avoir un aperçu de toute l'application", content_type=content_type
        )
        perm_analyst, created = Permission.objects.get_or_create(
            codename='can_analyst', name="Peut voir les rapports", content_type=content_type
        )
        perm_playlist_creator, created = Permission.objects.get_or_create(
            codename='can_create_playlists', name="Peut créer des playlists", content_type=content_type
        )

        # Ajouter les permissions aux groupes
        if not admin_group.permissions.contains(perm_admin):
            admin_group.permissions.add(perm_admin)
        if not analyst_group.permissions.contains(perm_analyst):
            analyst_group.permissions.add(perm_analyst)
        if not playlist_creator_group.permissions.contains(perm_playlist_creator):
            playlist_creator_group.permissions.add(perm_playlist_creator)

        # Créer les utilisateurs si nécessaire
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(username='admin', email='admin@example.com', password='admin')
            admin_user.groups.add(admin_group)

        if not User.objects.filter(username='analyst').exists():
            analyst_user = User.objects.create_user(username='analyst', email='analyst@example.com', password='analyst')
            analyst_user.groups.add(analyst_group)

        if not User.objects.filter(username='playlist_creator').exists():
            playlist_creator_user = User.objects.create_user(username='playlist_creator', email='playlist_creator@example.com', password='playlist_creator')
            playlist_creator_user.groups.add(playlist_creator_group)

        self.stdout.write(self.style.SUCCESS("Les utilisateurs ont été créés avec succès."))
