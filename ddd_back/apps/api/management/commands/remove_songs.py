from django.core.management.base import BaseCommand
from apps.api.models import Song

class Command(BaseCommand):
    help = "Supprime tous les enregistrements de Song."

    def handle(self, *args, **kwargs):
        count, _ = Song.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"{count} enregistrements supprimés."))
