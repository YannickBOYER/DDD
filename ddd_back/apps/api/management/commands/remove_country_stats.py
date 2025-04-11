from django.core.management.base import BaseCommand
from apps.api.models import CountryStats

class Command(BaseCommand):
    help = "Supprime tous les enregistrements de CountryStats."

    def handle(self, *args, **kwargs):
        count, _ = CountryStats.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"{count} enregistrements supprimés."))
