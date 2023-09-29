from .. import API, tables
from ..fs.compressor import Compressor
from core.library import api, default_storage, mkdirs, uuid


def upload(req, *args, **kwargs):
  ''' handle a file upload process '''

  # Authenticate User
  user = api.get_user(req)
  if user is None:
    return api.fail("Failed to authenticate user.")

  # Verify or create user file directory
  u_path = API.upload_dir(user)
  mkdirs(u_path, exist_ok=True)

  # Load file into memory
  f = req.FILES.get('file')
  f_uuid = uuid()
  f_dir = u_path / f_uuid
  f_path = f_dir / f.name
  f_mime_type = req.GET.get('mimeType')
  mkdirs(f_dir, exist_ok=True)

  # Save file to disk
  default_storage.save(f_path, f)

  # Compress file
  f = Compressor(file_dir=f_dir, absolute_file_path=f_path, mime_type=f_mime_type).compress()

  # Save file to Database
  tables.RDFSModel.objects.create(
    uuid=f_uuid,
    name=f['name'],
    ext=f['ext'],
    mime_type=f['mime_type'],
    size=f['size'],
    compressed_alias=f['compressed_alias'],
    compressed_size=f['compressed_size'],
    uploaded_by=user.data.uuid
  )

  # Complete process
  return api.data({"compressedSize": f['compressed_size']})
