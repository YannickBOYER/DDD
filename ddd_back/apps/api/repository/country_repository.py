from apps.api.models import CountryStats

class CountryRepository:
    @staticmethod
    def get_country_stats(country_name: str) -> CountryStats:
        """
        Retrieve country statistics by country name.
        """
        try:
            return CountryStats.objects.get(country=country_name)
        except CountryStats.DoesNotExist:
            return None

    @staticmethod
    def get_all_countries() -> list:
        """
        Retrieve all countries from the database.
        """
        return list(CountryStats.objects.values_list('country', flat=True))
