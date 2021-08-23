from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from os import environ

environ.__setitem__("DJANGO_SETTINGS_MODULE", (lambda value: value if value is not None else "Astromodel.settings.development")(environ.get("DJANGO_SETTINGS_MODULE")))

asgi_application = get_asgi_application()

import api.routing


application = ProtocolTypeRouter({
    'http': asgi_application,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(api.routing.websocket_urlpatterns)
            )
        ),
})
