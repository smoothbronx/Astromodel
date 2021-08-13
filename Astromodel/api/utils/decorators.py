from django.conf import settings
from django.http import JsonResponse
from .responses import access_denied

def validate(function):
    def wrapper(*args, **kwargs):
        return JsonResponse(access_denied, status=403, json_dumps_params={'indent': 4}) \
            if not (any(list(map(lambda data: data == settings.API_TOKEN,
                                 [args[-1].headers.get('access-token', None),
                                  kwargs.get('token', None)])))) else function(*args, **kwargs)
    return wrapper