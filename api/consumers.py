from json import dumps, loads
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from common.utils.handlers import KuramotoHandler, JSONHandler
from common.utils.responses import access_denied


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
        data = loads(text_data)
        if self.validate(data.get("token"), data.get("event")):
            await self.send(text_data=dumps({"message": await self.calculate(data.get("message")), "event": "server.response"}))
        else:
            await self.send(text_data=dumps(access_denied["asgi"]))
        