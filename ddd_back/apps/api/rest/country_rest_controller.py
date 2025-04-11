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

    def get(self, request):
        countries = self.countryRepository.get_all_countries()
        return Response({"countries": countries}, status=status.HTTP_200_OK)
    
    def get_songs(self, request, country):
        return Response({'songs': self.countryRepository.get_songs(country)}, status=status.HTTP_200_OK)
