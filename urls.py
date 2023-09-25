from . import API
from .endpoints.status import StatusConsumer

API.socket(
  "status",
  StatusConsumer,
  "Constant socket connection used to verify server status"
)
