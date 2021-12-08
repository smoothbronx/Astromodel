from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
from api.models import Query
 
class Command(BaseCommand): 
	def handle(self, *args, **kwargs):
		while not locals().get('database_connection', None):
        	try: database_connection = connections['default']
         	except OperationalError: sleep(5)
		else: Query.objects.all().delete()
