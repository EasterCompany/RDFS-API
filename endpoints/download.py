from wsgiref.util import FileWrapper
from core.library import api, exists, rmtree, HttpResponse
from core.model.user.tables import User

from .. import API, tables
from ..fs.decompressor import Decompressor


def download(req, user_uuid:str, file_uuid:str, *args, **kwargs):
  ''' Returns raw file data in a downloadable context '''
  file_owner = User(identifier=user_uuid)
  file_owner_dir = API.upload_dir(file_owner)
  file_record = tables.RDFSModel.objects.get(uuid=file_uuid, uploaded_by=file_owner.data.uuid)

  if file_record.privacy != 'public':
    user = api.get_user(req)
    if user is None:
      return api.fail("Failed to authenticate user.")
    if user.data.uuid != file_record.uploaded_by:
      return api.fail("You do not have access to this file.")

  if file_record is None:
    return api.fail("Requested file does not exist.")

  file_decom = Decompressor(file_record=file_record, user_dir=file_owner_dir)
  if not exists(file_decom.hot_path):
    file_decom.decompress()

  file_data = open(file_decom.hot_path, 'rb')
  rmtree(file_decom.hot_dir)
  response = HttpResponse(FileWrapper(file_data), content_type=file_record.mime_type)
  response['Content-Disposition'] = f'attachment; filename={file_record.name}{file_record.ext}'
  return response
