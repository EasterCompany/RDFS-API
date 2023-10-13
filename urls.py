from . import API
from .endpoints import generic, view, upload, download

# Endpoints
API.path("view/<str:file_uuid>", view.view, "Allows a user to view a file")
API.path("upload", upload.upload, "Allows a user to upload files")
API.path("download", download.download, "Allow a user to download files")

# Sockets
API.socket("info", generic.GenericConsumer, "Constant socket connection used to communicate generic data")
