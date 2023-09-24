from . import API
from .endpoints import status

API.socket(
  "status",
  status.StatusConsumer,
  "Constant socket connection used to verify server status"
)
