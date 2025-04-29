from apps.api.models import Song
from django.db.models import Q
from apps.api.models import CountryStats
from django.db.models import F, FloatField, ExpressionWrapper

class SongRepository:
    @staticmethod
    def find_by_name(music: str):
        return Song.objects.filter(name=music).all().first()


    @staticmethod
    def generate_playlist(country_source: str,
                      song_source: Song,
                      country_cible: str,
                      limit: int = 10) -> list:
        # —––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        # Récupération des stats des 2 pays
        src_stats = CountryStats.objects.filter(country=country_source).first()
        tgt_stats = CountryStats.objects.filter(country=country_cible).first()

        # Calcul des valeurs “cibles” par feature
        features = ['tempo', 'danceability', 'energy', 'valence', 'loudness', 'speechiness',
                    'acousticness', 'instrumentalness']
        target = {}
        for feat in features:
            ratio = getattr(tgt_stats, feat) / getattr(src_stats, feat)
            target[feat] = getattr(song_source, feat) * ratio

        # —––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        # Calcul de la distance euclidienne entre la source et la cible
        dist_sq = None
        for feat in features:
            expr = ExpressionWrapper(
                (F(feat) - target[feat])**2,
                output_field=FloatField()
            )
            dist_sq = expr if dist_sq is None else dist_sq + expr

        # Query filtrée par pays et ordonnée par distance
        qs = (
            Song.objects
            .filter(country_full=country_cible)
            .annotate(dist_sq=dist_sq)
            .order_by('dist_sq')[:limit]
        )

        # —––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        # Construction de la playlist
        playlist = []
        for item in qs:
            entry = {'name': item.name, 'artists': item.artists}
            if entry not in playlist:
                playlist.append(entry)

        # On retire la source si elle apparaît
        # src_entry = {'name': song_source.name, 'artists': song_source.artists}
        # if src_entry in playlist:
        #     playlist.remove(src_entry)

        return playlist