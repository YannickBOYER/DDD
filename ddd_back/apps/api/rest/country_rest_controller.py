from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..repository.country_repository import CountryRepository
from rest_framework.viewsets import ViewSet


class CountryRestController(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.countryRepository = CountryRepository()

    def get_names(self, request):
        authorized_groups = ['admin', 'playlist_creator', 'analyst']

        groups = request.user.groups.values_list('name', flat=True)

        if not any(group in authorized_groups for group in groups):
            return Response({"detail": "Vous n'avez pas le rôle requis pour accéder à cet endpoint."}, status=status.HTTP_403_FORBIDDEN)

        countries = self.countryRepository.get_all_countries_names()
        return Response({"countries": countries}, status=status.HTTP_200_OK)
    
    def get(self, request):
        authorized_groups = ['admin', 'analyst']
        groups = request.user.groups.values_list('name', flat=True)

        if not any(group in authorized_groups for group in groups):
            return Response({"detail": "Vous n'avez pas le rôle requis pour accéder à cet endpoint."}, status=status.HTTP_403_FORBIDDEN)

        countries = self.countryRepository.get_all_countries()
        return Response({"countries": countries}, status=status.HTTP_200_OK)

    
    def get_songs(self, request, country):
        authorized_groups = ['admin', 'playlist_creator', 'analyst']
        groups = request.user.groups.values_list('name', flat=True)

        if not any(group in authorized_groups for group in groups):
            return Response({"detail": "Vous n'avez pas le rôle requis pour accéder à cet endpoint."}, status=status.HTTP_403_FORBIDDEN)

        return Response({'songs': self.countryRepository.get_songs(country)}, status=status.HTTP_200_OK)
