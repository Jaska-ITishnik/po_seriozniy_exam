from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = "Run migrations on all configured databases"

    def handle(self, *args, **kwargs):
        databases = settings.DATABASES.keys()
        for db in databases:
            self.stdout.write(self.style.SUCCESS(f'Running migrations for {db}...'))
            call_command('migrate', database=db)
            self.stdout.write(self.style.SUCCESS(f'Migrations completed for {db}.'))
