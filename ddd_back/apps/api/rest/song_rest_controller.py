from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json
from rest_framework.authentication import TokenAuthentication
from ..service.song_service import SongService

class SongRestController(ViewSet):
    authentication_classes = [TokenAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.songService = SongService()

    def generate_playlist(self, request):
        authorized_groups = ['ddd_admin', 'ddd_playlist_creator']
        groups = request.user.groups.values_list('name', flat=True)

        if not any(group in authorized_groups for group in groups):
            return Response({"detail": "Vous n'avez pas le rôle requis pour accéder à cet endpoint."}, status=status.HTTP_403_FORBIDDEN)

        authorized_groups = ['ddd_admin', 'ddd_playlist_creator']
        groups = request.user.groups.values_list('name', flat=True)

        if not any(group in authorized_groups for group in groups):
            return Response({"detail": "Vous n'avez pas le rôle requis pour accéder à cet endpoint."}, status=status.HTTP_403_FORBIDDEN)

        data = json.loads(request.body)
        country_source = data['country_source']
        music = data['music']
        country_cible = data['country_cible']
        response = self.songService.generate_playlist(country_source, music, country_cible)

        return Response(response, status=status.HTTP_200_OK)

