from core.library import AsyncJsonWebsocketConsumer


class StatusConsumer(AsyncJsonWebsocketConsumer):
  ''' Web Socket Interface for the Process View '''

  async def connect(self, *args, **kwargs):
    await self.accept()
