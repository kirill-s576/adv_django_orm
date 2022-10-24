from django.core.management.base import BaseCommand, CommandError
from shop.scripts.clean_up_demo_db import clean_up_db


class Command(BaseCommand):
    help = 'Clean-up database for Shop app'

    def handle(self, *args, **options):
        clean_up_db()
        self.stdout.write(self.style.SUCCESS('Db cleaned successfully'))
