from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding DB ...")
