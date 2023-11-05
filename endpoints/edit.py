import base64
from core.library import api, exists, rmtree, redis

from .. import API, tables
from ..fs.decompressor import Decompressor


def edit(req, *args, **kwargs):
  ''' Edits a file record in the database based on the given context '''
  user = api.get_user(req)
  json = api.get_json(req)

  if user is None:
    return api.fail("Failed to authenticate user.")

  file_record = tables.RDFSModel.objects.get(uuid=json['file_uuid'], uploaded_by=user.data.uuid)

  if file_record is None:
    return api.fail("Requested file does not exist.")

  if 'privacy' not in json:
    json['privacy'] = file_record.privacy

  if json['privacy'] not in ['public', 'private']:
    return api.fail("Invalid privacy setting.")

  file_record.privacy = json['privacy']
  file_record.save()

  return api.success()
