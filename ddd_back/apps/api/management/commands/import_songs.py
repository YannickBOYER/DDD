from django.core.management.base import BaseCommand
from apps.api.models import Song
import pandas as pd
from datetime import datetime

class Command(BaseCommand):
    help = "Import songs from a cleaned CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the cleaned CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            self.stderr.write(f"Erreur lors de la lecture du fichier : {e}")
            return

        imported_count = 0
        for _, row in df.iterrows():
            try:
                Song.objects.create(
                    spotify_id=row['spotify_id'],
                    name=row['name'],
                    artists=row['artists'],
                    country=row['country'],
                    popularity=int(row['popularity']),
                    is_explicit=row['is_explicit'] in [True, 'True', 'true', 1],
                    duration_ms=int(row['duration_ms']),
                    album_name=row['album_name'],
                    album_release_date=datetime.strptime(str(row['album_release_date']), '%Y-%m-%d'),
                    danceability=float(row['danceability']),
                    energy=float(row['energy']),
                    key=int(row['key']),
                    loudness=float(row['loudness']),
                    mode=int(row['mode']),
                    speechiness=float(row['speechiness']),
                    acousticness=float(row['acousticness']),
                    instrumentalness=float(row['instrumentalness']),
                    liveness=float(row['liveness']),
                    valence=float(row['valence']),
                    tempo=float(row['tempo']),
                    time_signature=int(row['time_signature']),
                    country_full=row['country_full']
                )
                imported_count += 1
            except Exception as e:
                self.stderr.write(f"Erreur sur une ligne : {e}")

        self.stdout.write(self.style.SUCCESS(f"{imported_count} chansons importées avec succès."))
