from apps.api.models import Song
from django.db.models import Q
from apps.api.models import CountryStats

class SongRepository:
    @staticmethod
    def find_by_name(music: str):
        return Song.objects.filter(name=music).all().first()


    @staticmethod
    def generate_playlist(country_source: str, song_source: Song, country_cible: str,) -> list:
        # On récupère les moyennes du pays source
        country_source_data = CountryStats.objects.filter(country=country_source).first()
        country_cible_data = CountryStats.objects.filter(country=country_cible).first()

        # On récupère les propriétés de la musique source
        min_tempo = song_source.tempo * (country_cible_data.tempo / country_source_data.tempo)
        max_tempo = song_source.tempo * (country_cible_data.tempo / country_source_data.tempo)
        min_danceability = song_source.danceability * (country_cible_data.danceability / country_source_data.danceability)
        max_danceability = song_source.danceability * (country_cible_data.danceability / country_source_data.danceability)
        min_energy = song_source.energy * (country_cible_data.energy / country_source_data.energy)
        max_energy = song_source.energy * (country_cible_data.energy / country_source_data.energy)
        min_valence = song_source.valence * (country_cible_data.valence / country_source_data.valence)
        max_valence = song_source.valence * (country_cible_data.valence / country_source_data.valence)

        

        min_tempo = min_tempo * (1 - 0.15)
        max_tempo = max_tempo * (1 + 0.15)
        min_danceability = min_danceability * (1 - 0.15)
        max_danceability = max_danceability * (1 + 0.15)
        min_energy = min_energy * (1 - 0.15)
        max_energy = max_energy * (1 + 0.15)
        min_valence = min_valence * (1 - 0.15)
        max_valence = max_valence * (1 + 0.15)

        songs = Song.objects.filter(
            Q(country_full=country_cible),
            # Q(mode=song_source.mode),
            Q(tempo__gte=min_tempo),
            Q(tempo__lte=max_tempo),
            Q(danceability__gte=min_danceability),
            Q(danceability__lte=max_danceability),
            Q(energy__gte=min_energy),
            Q(energy__lte=max_energy),
            Q(valence__gte=min_valence),
            Q(valence__lte=max_valence),
        ).all()

        playlist = []
        for item in songs:
            song = ({
                'name': item.name,
                'artists': item.artists,
                #'tempo': item.tempo,
                #'mode': item.mode,
                #'danceability': item.danceability,
                #'energy': item.energy,
                #'valence': item.valence,
            })
            # Distinct
            if song not in playlist:
                playlist.append(song)

        song_source_format = ({'name':song_source.name, 'artists': song_source.artists})
        if song_source_format in playlist:
            playlist.remove(song_source_format)
        
        return playlist