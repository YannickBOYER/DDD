from django.core.management.base import BaseCommand
from apps.api.models import CountryStats
import pandas as pd

class Command(BaseCommand):
    help = "Import country stats from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the country stats CSV file')

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
                obj, created = CountryStats.objects.update_or_create(
                    country=row['country'],  # Critère de recherche (ici le pays)
                    defaults={  # Les valeurs à mettre à jour ou à créer
                        'popularity': float(row['popularity']),
                        'is_explicit': float(row['is_explicit']),
                        'danceability': float(row['danceability']),
                        'energy': float(row['energy']),
                        'loudness': float(row['loudness']),
                        'mode': float(row['mode']),
                        'speechiness': float(row['speechiness']),
                        'acousticness': float(row['acousticness']),
                        'instrumentalness': float(row['instrumentalness']),
                        'liveness': float(row['liveness']),
                        'valence': float(row['valence']),
                        'tempo': float(row['tempo']),
                        'social_media_users': int(row['social_media_users']),
                        'social_media_pct': float(row['social_media_pct']),
                        'total_population': int(row['Total']),
                        'age_65_plus': float(row['65+']),
                        'age_25_64': float(row['25-64 years']),
                        'age_15_24': float(row['15-24 years']),
                        'age_5_14': float(row['5-14 years']),
                        'age_0_4': float(row['0-4 years']),
                    }
                )
                if created:
                    pass
                else:
                    self.stdout.write(self.style.SUCCESS(f"{row['country']} mis à jour avec succès."))
                imported_count += 1
            except Exception as e:
                self.stderr.write(f"Erreur sur une ligne : {e}")

        self.stdout.write(self.style.SUCCESS(f"{imported_count} pays importés ou mis à jour avec succès."))
