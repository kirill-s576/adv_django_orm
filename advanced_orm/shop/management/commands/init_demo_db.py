from django.core.management.base import BaseCommand, CommandError
from shop.scripts.init_demo_db import init_db


class Command(BaseCommand):
    help = 'Initialize demo database for Shop app'

    def handle(self, *args, **options):
        init_db()
        self.stdout.write(self.style.SUCCESS('Db initialized successfully'))
