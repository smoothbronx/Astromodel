from django.conf import settings
from django.http import HttpResponse


# DECORATORS
def validate(function):
    def wrapper(*args, **kwargs):
        return HttpResponse('Access denied') if kwargs['token'] != settings.API_TOKEN else function(*args, **kwargs)
    return wrapper
