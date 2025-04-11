from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.api.models import CountryStats

class CountryRestController(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Make a database call to get the list of countries in the api_countrystats table
        countries = CountryStats.objects.values_list('country', flat=True)
        return Response({"countries": list(countries)}, status=200)
