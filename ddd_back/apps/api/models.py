from django.db import models

# Create your models here.
class Song(models.Model):
    spotify_id = models.CharField(max_length=50)
    country_full = models.CharField(max_length=50)

    country = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    artists = models.CharField(max_length=300)
    popularity = models.IntegerField()
    is_explicit = models.BooleanField()
    duration_ms = models.IntegerField()
    album_name = models.CharField(max_length=200)
    album_release_date = models.DateField(null=True, blank=True)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    speechiness = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.IntegerField()

    class Meta:
        unique_together = (('spotify_id', 'country_full'),)

class CountryStats(models.Model):
    country = models.CharField(max_length=100, unique=True)  # Nom unique du pays
    # Moyennes musicales
    popularity = models.FloatField()
    is_explicit = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    loudness = models.FloatField()
    mode = models.FloatField()
    speechiness = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()

    # Données démographiques
    social_media_users = models.BigIntegerField()
    social_media_pct = models.FloatField()
    total_population = models.BigIntegerField()
    age_65_plus = models.FloatField()
    age_25_64 = models.FloatField()
    age_15_24 = models.FloatField()
    age_5_14 = models.FloatField()
    age_0_4 = models.FloatField()

    def __str__(self):
        return self.country
