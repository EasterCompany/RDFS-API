import base64
from .. import API, tables
from ..fs.decompressor import Decompressor
from core.library import api, exists, HttpResponse


def view(req, *args, **kwargs):
  ''' endpoint which returns an html view containing an embedded file '''
  try:
    user = api.get_user(req)
    json = api.get_json(req)

    user_dir = API.upload_dir(user)
    file_record = tables.RDFSModel.objects.get(uuid=json['uuid'], uploaded_by=user.data.uuid)

    if file_record is None:
      return api.fail("Requested file does not exist.")

    file_decom = Decompressor(file_record=file_record, user_dir=user_dir)
    if not exists(file_decom.hot_path):
      file_decom.decompress()

    with open(file_decom.hot_path, 'rb') as decom_f:
      file_data = base64.b64encode(decom_f.read())

    return HttpResponse(file_data)
  except Exception as error:
    return api.error(error)
