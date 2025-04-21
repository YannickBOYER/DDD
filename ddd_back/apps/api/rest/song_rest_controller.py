from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json

from ..service.song_service import SongService

class SongRestController(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.songService = SongService()

    def generate_playlist(self, request):
        data = json.loads(request.body)
        country_source = data['country_source']
        music = data['music']
        country_cible = data['country_cible']
        response = self.songService.generate_playlist(country_source, music, country_cible)

        return Response(response, status=status.HTTP_200_OK)