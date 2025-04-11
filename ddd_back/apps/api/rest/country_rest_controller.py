from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..repository.country_repository import CountryRepository


class CountryRestController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.countryRepository = CountryRepository()

    def get(self, request):
        countries = self.countryRepository.get_all_countries()
        return Response({"countries": countries}, status=status.HTTP_200_OK)
