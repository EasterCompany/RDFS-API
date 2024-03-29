from core.library import AsyncJsonWebsocketConsumer, database_sync_to_async
from ..tables import RDFSModel


class GenericConsumer(AsyncJsonWebsocketConsumer):
  ''' Web Socket Interface for the Process View '''

  async def connect(self, *args, **kwargs):
    await self.accept()

  async def receive_json(self, content=None):
    user_uuid = content['uuid']
    user_data = await self.get_user_data(user_uuid=user_uuid)
    await self.send_json(user_data)

  @database_sync_to_async
  def get_user_data(self, user_uuid):
    user_file_objects = RDFSModel.objects.filter(uploaded_by=user_uuid)
    user_data = {
      "userFiles": []
    }

    for f in user_file_objects:
      user_data['userFiles'].append({
        "uuid": f.uuid,
        "name": f.name,
        "ext": f.ext,
        "mimeType": f.mime_type,
        "size": f.size,
        "compressedSize": f.compressed_size,
        "uploadedBy": f.uploaded_by,
        "category": f.category,
        "privacy": f.privacy
      })

    return user_data
