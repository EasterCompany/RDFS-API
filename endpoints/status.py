from core.library import AsyncWebsocketConsumer


class StatusConsumer(AsyncWebsocketConsumer):
  ''' Web Socket Interface for the Process View '''

  async def connect(self, *args, **kwargs):
    await self.accept()
