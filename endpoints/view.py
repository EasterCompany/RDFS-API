import base64
from core.library import api, exists

from .. import API, tables
from ..fs.decompressor import Decompressor


def view(req, file_uuid:str, *args, **kwargs):
  ''' Returns an HTML view containing an embedded file. '''
  user = api.get_user(req)
  user_dir = API.upload_dir(user)
  file_record = tables.RDFSModel.objects.get(uuid=file_uuid, uploaded_by=user.data.uuid)

  if file_record is None:
    return api.fail("Requested file does not exist.")

  file_decom = Decompressor(file_record=file_record, user_dir=user_dir)
  if not exists(file_decom.hot_path):
    file_decom.decompress()

  with open(file_decom.hot_path, 'rb') as decom_f:
    return api.data(
      f"data:{file_record.mime_type};base64,{base64.b64encode(decom_f.read()).decode()}"
    )
