from apps.api.models import CountryStats
from apps.api.models import Song

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
    def get_all_countries_names() -> list:
        """
        Retrieve all countries from the database.
        """
        return list(CountryStats.objects.values_list('country', flat=True))

    @staticmethod
    def get_songs(country) -> list:
        songs_names = []
        songs = Song.objects.filter(country_full=country).all()
        for song in songs:
            songs_names.append({
                'name': song.name,
                'artists': song.artists
            })
        return songs_names
