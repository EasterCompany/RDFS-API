import os
from .. import API, tables
from core.library import api, default_storage, mkdirs, uuid


def upload(req, *args, **kwargs):

  # Authenticate User
  user = api.get_user(req)
  if user is None:
    return api.fail("Failed to authenticate user.")

  # Verify or Create User File Directory
  u_path = API.UPLOAD_DIR / user.data.uuid / 'rdfs'
  mkdirs(u_path, exist_ok=True)

  # Save File to Storage
  f = req.FILES.get('file')
  f_uuid = uuid()
  f_path = u_path / f_uuid
  mkdirs(f_path, exist_ok=True)
  default_storage.save(f_path / f.name, f)

  # Save File to Database
  f_name, f_ext = os.path.splitext(f.name)
  f_size = os.path.getsize(f_path / f.name)
  tables.RDFSModel.objects.create(
    uuid=f_uuid,
    name=f_name,
    ext=f_ext,
    size=f_size,
    uploaded_by=user.data.uuid
  )

  return api.success()
