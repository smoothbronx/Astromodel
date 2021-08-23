from os import environ
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


environ.__setitem__("DJANGO_SETTINGS_MODULE", (lambda value: value if value is not None else "Astromodel.settings.development")(environ.get("DJANGO_SETTINGS_MODULE")))

application = DjangoWhiteNoise(get_wsgi_application())
