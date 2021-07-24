from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path('kuramoto/', consumers.KuramotoConsumer.as_asgi()),
]