from .. import API, tables
from ..fs.compressor import Compressor
from core.library import api, default_storage, mkdirs, uuid, getsize, rmtree, exists


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

  try:
    # Save file to disk
    default_storage.save(f_path, f)
    f_size = getsize(f_path)

    # Compress file
    f = Compressor(
      uuid=f_uuid,
      user_path=u_path,
      absolute_file_path=f_path
    )
    f.compress()

    # Save file to Database
    tables.RDFSModel.objects.create(
      uuid=f_uuid,
      name=f.name,
      ext=f.ext,
      mime_type=f_mime_type,
      size=f_size,
      compressed_ext=f.compressed_ext,
      compressed_size=f.compressed_size,
      uploaded_by=user.data.uuid
    )

    # Complete process
    return api.data({
      "uploadSize": f_size,
      "compressedSize": f.compressed_size
    })

  # Fail process
  except Exception as error:
    if exists(f_dir):
      rmtree(f_dir)
    return api.error(error)
