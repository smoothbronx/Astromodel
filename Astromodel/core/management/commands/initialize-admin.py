from os import environ
from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        superusers = User.objects.filter(is_superuser=True)
        
        if superusers.count():
            superusers.delete()
            
        User.objects.create_superuser(
                environ.get("DJANGO_ADMIN_USERNAME", "admin"),
                environ.get("DJANGO_ADMIN_EMAIL", "admin@example.com"),
                environ.get("DJANGO_ADMIN_PASSWORD", "password")
            ).save()
        