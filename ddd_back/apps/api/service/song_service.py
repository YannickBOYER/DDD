from ..repository.song_repository import SongRepository

class SongService:
    def __init__(self):
        self.song_repository = SongRepository()

    def generate_playlist(self, country_source: str, music: str, country_cible: str):
        song_source = self.song_repository.find_by_name(music)
        playlist = self.song_repository.generate_playlist(country_source, song_source, country_cible)

        tempo = f"{round(song_source.tempo)}bpm"
        mode = "majeur" if song_source.mode == 1 else "mineur"
        danceablility = f"{round(song_source.danceability, 3) * 100}%"
        energy = f"{round(song_source.energy, 1) * 100}%"
        valence = f"{round(song_source.valence, 3) * 100}%"

        return ({
            'song_source': song_source.name,
            'song_source_artists': song_source.artists,
            'song_source_artists': song_source.artists,
            'tempo': tempo,
            'mode': mode,
            'danceability': danceablility,
            'energy': energy,
            'valence': valence,
            'playlist_generated': playlist,
        })