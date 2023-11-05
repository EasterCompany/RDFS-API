from . import API
from .endpoints import generic, view, upload, download, edit

# Endpoints
API.path("view/<str:file_uuid>", view.view, "Allows a user to view a file")
API.path("upload", upload.upload, "Allows a user to upload files")
API.path("download/<str:user_uuid>/<str:file_uuid>", download.download, "Allow a user to download files")
API.path("edit", edit.edit, "Allows a user to edit a file")

# Sockets
API.socket("info", generic.GenericConsumer, "Constant socket connection used to communicate generic data")
