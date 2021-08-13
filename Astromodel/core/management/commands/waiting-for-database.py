from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
 
class Command(BaseCommand): 
    def handle(self, *args, **kwargs):
        sleep(15)
        while not locals().get('database_connection', None):
            try: database_connection = connections['default']
            except OperationalError: sleep(5)