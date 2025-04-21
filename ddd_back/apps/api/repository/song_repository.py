from apps.api.models import Song
from django.db.models import Q

class SongRepository:
    @staticmethod
    def find_by_name(music: str):
        return Song.objects.filter(name=music).all().first()


    @staticmethod
    def generate_playlist(country_source: str, song_source: Song, country_cible: str,) -> list:
        # On récupère les propriétés de la musique source
        min_tempo = song_source.tempo * (1 - 0.10)
        max_tempo = song_source.tempo * (1 + 0.10)
        min_danceability = song_source.danceability * (1 - 0.10)
        max_danceability = song_source.danceability * (1 + 0.10)
        min_energy = song_source.energy * (1 - 0.10)
        max_energy = song_source.energy * (1 + 0.10)
        min_valence = song_source.valence * (1 - 0.10)
        max_valence = song_source.valence * (1 + 0.10)

        songs = Song.objects.filter(
            Q(country_full=country_cible),
            Q(mode=song_source.mode),
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