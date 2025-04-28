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
    def get_all_countries() -> list:
        """
        Retrieve all countries from the database.
        """
        countries = CountryStats.objects.all()
        response = []
        for country in countries:
            response.append({
                'name': country.country,
                'popularity': country.popularity,
                'is_explicit': country.is_explicit,
                'danceability': country.danceability,
                'energy': country.energy,
                'loudness': country.loudness,
                'mode': country.mode,
                'speechiness': country.speechiness,
                'acousticness': country.acousticness,
                'instrumentalness': country.instrumentalness,
                'liveness': country.liveness,
                'valence': country.valence,
                'tempo': country.tempo,
                'social_media_users': country.social_media_users,
                'social_media_pct': country.social_media_pct,
                'total_population': country.total_population,
                'age_65_plus': country.age_65_plus,
                'age_25_64': country.age_25_64,
                'age_15_24': country.age_15_24,
                'age_5_14': country.age_5_14,
                'age_0_4': country.age_0_4,
            })
        return response

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
