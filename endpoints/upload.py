import os
from .. import API, tables
from core.library import api, default_storage, mkdirs, uuid, console, remove


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
  mkdirs(f_dir, exist_ok=True)

  # Save file to disk
  default_storage.save(f_path, f)

  # Compress file
  console.input(f"lrzip -z {f.name}", cwd=f_dir)

  # Save file to Database
  f_name, f_ext = os.path.splitext(f.name)
  tables.RDFSModel.objects.create(
    uuid=f_uuid,
    name=f_name,
    ext=f_ext,
    mime_type=req.GET.get('mimeType'),
    size=os.path.getsize(f_path),
    compressed_size=os.path.getsize(f"{f_path}.lrz"),
    uploaded_by=user.data.uuid
  )

  # Delete original
  remove(f_path)

  # Retrieve file from database
  f_db = tables.RDFSModel.objects.get(uuid=f_uuid)

  # Complete process
  return api.data({
    "url": f_db.source_path(),
    "compressedSize": f_db.compressed_size
  })
