from django.core.management.base import BaseCommand
from utils import data_loader

class Command(BaseCommand):
    help = 'add dam data'

    def handle(self, **options):
        # print("Hello")
        data_loader.run()
