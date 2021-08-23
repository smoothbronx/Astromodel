from json import dumps, loads
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from common.utils.handlers import KuramotoHandler, JSONHandler
from .utils.responses import access_denied
from .utils.functions import createQuery
from channels.db import database_sync_to_async

class KuramotoConsumerBase:
    kuramoto = KuramotoHandler()
    
    async def validate(self, token: str, event: str):
        return True if token == settings.API_TOKEN and event == "client.request" else False
    
    async def calculate(self, data) -> dict:
        return self.kuramoto.setData(data).setHandler(JSONHandler).build()
    

class KuramotoConsumer(AsyncWebsocketConsumer, KuramotoConsumerBase):
    async def connect(self):
        await self.accept()
        await self.send(text_data=dumps({"event": "server.accept"}))
         
    async def disconnect(self, code):
        pass
    
    async def receive(self, text_data):
        request = loads(text_data)
        response = await self.calculate(request.get("message"))
        
        await database_sync_to_async(createQuery)("websocket", request, response)
        await self.send(text_data=dumps({"message": response, "event": "server.response"})) \
            if self.validate(request.get("token"), request.get("event")) \
            else self.send(text_data=dumps(access_denied["asgi"]))
